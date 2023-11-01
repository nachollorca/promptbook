def create_tutorial(
		interests: str,  # required
		objective: str,  # required
		duration: str = "10 minutes",  # default value
		skill_level: str = "beginner",  # default value
		tools: str = None,  # optional
		unique: str = None,  # optional
		video_framework: str = "1. Introduction\n2. Main Content\n3. Conclusion"  # default value
) -> str:
	prompt = """
Please suggest a tutorial video idea that is both engaging and educational. Here are the details:
- Audience Interests: {interests}
- Objective: {objective}
- Duration: {duration}
- Skill Level: {skill_level}
"""
	if tools is not None:
		prompt = prompt + f"- Tools/Software Required: {tools}\n"

	if unique is not None:
		prompt = prompt + f"- Unique Angle: {unique}\n"
		
	prompt = prompt + f"""
Based on these details, provide an outline for the video that covers the following:
{video_framework}

List the steps to be covered for each section of the outline, and also indicate any key points or tips that should be included.
"""
	
	return prompt.format(
		interests=interests,
		objective=objective,
		duration=duration,
		skill_level=skill_level,
		tools=tools if tools is not None else "",
		unique=unique if unique is not None else "",
		video_framework=video_framework
	)
# UI details
	_title = "Tutorial Video Idea Generator"
	_author = "ChatGPT"
	_description = "This recipe generates a tailored prompt for creating tutorial video ideas."
	_ui = {
		"interests": {
			"text": "What are the audience's interests?",
			"help": "Specify the interests to tailor the video content.",
			"suggestions": "coding, cooking, DIY"
		},
		"objective": {
			"text": "What is the objective of the video?",
			"help": "Specify what you aim to achieve with this video.",
			"suggestions": "How to set up Python, Cooking Pasta"
		},
		"duration": {
			"text": "What is the intended duration?",
			"help": "Specify the video length.",
			"suggestions": "5 minutes, 10 minutes"
		},
		"skill_level": {
			"text": "What is the skill level of the audience?",
			"help": "Specify the skill level.",
			"suggestions": "Beginner, Intermediate, Advanced"
		},
		"tools": {
			"text": "What tools or software are required?",
			"help": "Optional: specify the tools needed.",
			"suggestions": "Python, Cooking utensils"
		},
		"unique": {
			"text": "What is the unique angle?",
			"help": "Optional: specify a unique angle for the tutorial.",
			"suggestions": "Dashboard for eCommerce, Vegan Pasta"
		},
		"video_framework": {
				"text": "What is the video outline?",
				"help": "Specify the framework for the video.",
				"suggestions": "Introduction, Topic 1, Topic 2, Topic 3, Conclusion"
			}
		}	