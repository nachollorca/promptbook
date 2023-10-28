import streamlit as st
import os
import importlib.util
import sys
import inspect
from inspect import cleandoc
from prompt import launch_prompt, get_token_cost
from utils import are_required_filled

# set page
st.set_page_config(page_title="Promptbook", page_icon="media/logo.png", initial_sidebar_state="collapsed")
st.image("media/head.png", use_column_width=True)
with st.sidebar:
    """
# [Promptbook UI](https://github.com/nachollorca/promptbook/)
Do you find yourself writing the same kind of prompts again and again into ChatGPT?
Work your most used prompts into a comfy graphic user interface with just a few lines of code.

Promptbook allows you to:
 - Have a customizable UI from a simple prompt-building Python function
 - Store your GUI-prompts to reuse them on a click
 - Use fantastic recipe ideas from other contributors
 
## How it works
**Promptbook** is built upon Python function signatures and type hints. Then, Streamlit is used to provide a graphic interface.

In essence, a parser reads the prompt-generating function, identifies the arguments and creates according streamlit input widgets in the application.

Lastly, a Prompt class queries the OpenAI API and computes the answer, together with its token context and resulting cost.

## How to use
**To use the current recipes just get to play around in here.** If you do not have an OpenAI API key to launch the prompts, you can generate them and copy-paste into [ChatGPT](https://chat.openai.com/).

To create your own recipes, head over to [`docs/contribute.md`](https://github.com/nachollorca/promptbook/blob/main/docs/contribute.md). To learn best practices on prompt engineering, I recommend [this compendium](https://www.promptingguide.ai/introduction/tips).
"""

with st.expander("**:bookmark_tabs: Cookbook index**", expanded=True):
    # load and choose recipe
    recipes = sorted([item.strip(".py") for item in os.listdir("recipes") if item.endswith(".py")])
    recipe = st.selectbox(label="Choose a recipe", options=recipes)
    st.caption(f":link:[Check recipe source code](https://github.com/nachollorca/promptbook/blob/main/recipes/{recipe}.py)")

    # import chosen recipe
    spec = importlib.util.spec_from_file_location("recipe", f"recipes/{recipe}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["recipe"] = module
    spec.loader.exec_module(module)
    function = getattr(module, recipe)
    ui = getattr(module, "_ui", None)
    signature = inspect.signature(function)

    # introduce user interface
    if getattr(module, "_title", None) is not None:
        st.write(f'### {getattr(module, "_title")}')
    if getattr(module, "_author", None) is not None:
        st.caption(f'By {getattr(module, "_author")}')
    if getattr(module, "_description", None) is not None:
        st.write(getattr(module, "_description"))

    # create dictionary to parse arguments and ui info
    params = {}
    for name, hint in signature.parameters.items():
        # get parameter name, type and default value
        params[name] = {}
        params[name]["type"] = hint.annotation
        params[name]["default"] = hint.default

        # get information for the ui
        if isinstance(hint.default, type(inspect.Parameter.empty)):
            params[name]["required"] = True
            params[name]["label"] = f"**{name.capitalize()}** (required)"
        else:
            params[name]["required"] = False
            params[name]["label"] = f"**{name.capitalize()}** (optional, defaults to `{hint.default}`)"

        if ui is not None and name in ui.keys():
            params[name].update(ui[name])

messages = []
with st.expander("**:green_salad: Ingredients**", expanded=True):
    # grab arguments for the function and create user interface
    args = {}
    for arg, info in params.items():
        if info.get("text", None) is not None:
            st.write(info.get("text"))
        if str(info["type"]) in ["<class 'int'>", "<class 'float'>"]:
            args[arg] = st.number_input(
                label=info["label"],
                help=info.get("help", None),
                placeholder=info.get("suggestions", None),
            )
        else:
            args[arg] = st.text_area(
                label=info["label"],
                help=info.get("help", None),
                placeholder=info.get("suggestions", None),
            )

        # TODO: make input fields for other class types i.e. multiselect for lists

    # fill empty fields with default values
    for k, v in args.items():
        if v in ["", None]:
            args[k] = params[k]["default"]

    # generate prompt
    prompt = cleandoc(function(**args))

    # inspect/tune prompt
    c1, c2 = st.columns(2)
    if c1.button("Visualize prompt", use_container_width=True):
        if are_required_filled(args, params):
            st.markdown(prompt)
        else:
            st.warning("Please fill in all required values.")

    if c2.button("Fine-tune prompt", use_container_width=True):
        if are_required_filled(args, params):
            prompt = st.text_area("Edit prompt", value=prompt, label_visibility="hidden")
        else:
            st.warning("Please fill in all required values.")


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.expander("**:fire: Kitchen**", expanded=True):
    c1, c2 = st.columns(2)

    model = c1.selectbox("Model", options=["gpt-4", "gpt-3.5-turbo"])
    api_key = c2.text_input("OpenAI API key", type="password", placeholder="This will never be stored", help="If you do not have one, simply click on `Visualize prompt` above and copy paste the generated prompt into [ChatGPT]()")
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, step=0.1, value=0.0, help="Controls the “creativity” or randomness of the output. Higher temperatures (e.g., 0.7) result in more diverse and creative output (and potentially less coherent), while a lower temperature (e.g., 0.2) makes the output more deterministic and focused.")

    if st.button("Launch prompt", use_container_width=True):
        if not are_required_filled(args, params):
            st.warning("Please fill in all required values.")
        else:
            with st.spinner("**:gear:** on it..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                output = launch_prompt(st.session_state.messages, api_key, model, temperature)
                st.session_state.messages.append({"role": "assistant", "content": output})
                in_cost = get_token_cost(prompt, model, "input")
                out_cost = get_token_cost(output, model, "output")

            c1, c2 = st.columns(2)
            c1.metric("**Tokens** (input/output)", f'{in_cost["tokens"]} / {out_cost["tokens"]}')
            c2.metric("**Cost**", f'{round(in_cost["cost"] + out_cost["cost"], 5)} $')


if st.session_state.messages != []:
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if user_reply := st.chat_input("Continue interacting with the AI."):
        st.session_state.messages.append({"role": "user", "content": user_reply})
        with st.chat_message("user"):
            st.write(user_reply)

        ai_reply = launch_prompt(st.session_state.messages, api_key, model, temperature)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        with st.chat_message("assistant"):
            st.write(ai_reply)

