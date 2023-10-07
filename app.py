import streamlit as st
import os
import importlib.util
import sys
import inspect
from inspect import cleandoc
from prompt import launch_prompt

# set page metadata
st.set_page_config(page_title="Promptbook")

with st.expander("**:bookmark_tabs: Cookbook index**", expanded=True):
    # load and choose recipe
    recipes = [item.strip(".py") for item in os.listdir("recipes") if item.endswith(".py")]
    recipe = st.selectbox(label="Choose a recipe", options=recipes)

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


with st.expander("**:cook: Kitchen**", expanded=True):
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

    # inspect prompt
    c1, c2 = st.columns(2)
    if c1.button("Visualize prompt", use_container_width=True):
        st.markdown(prompt)
    if c2.button("Fine-tune prompt", use_container_width=True):
        prompt = st.text_area("Edit prompt", value=prompt)


with st.expander("**:fork_and_knife: Table**", expanded=True):
    c1, c2 = st.columns(2)

    model = c1.selectbox("Model", options=["gpt-4", "gpt-3.5-turbo"])
    api_key = c2.text_input("OpenAI API key", type="password", placeholder="This will never be stored")

    if st.button("Launch prompt", use_container_width=True):
        with st.spinner("**:gear:** on it..."):
            output = launch_prompt(prompt, api_key, model)
        st.write(output)