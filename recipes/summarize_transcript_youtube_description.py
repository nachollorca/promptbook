def summarize_transcript_youtube_description(
		transcript, 
		tone='professional', 
		length='concise', 
		style='emoji bulleted', 
		keywords='', 
		reading_level='6th grade'
	):
	prompt = f"""
Generate a video description for the transcript below that includes keywords {keywords}. Its length should be {length} and written in a {tone} tone of voice. The format of content should be arranged in the style of {style}. The reading level should be targeted to {reading_level}.

```
{transcript}
```
"""

	return prompt

# Optional UI dict
_ui = {
	"transcript": {"text": "Enter the video transcript.", "help": "This is a required field."},
	"tone": {"help": "Tone of voice", "suggestions": "Professional, Casual, Conversational"},
	"length": {"help": "Desired length", "suggestions": "Short, Medium, Long"},
	"style": {"help": "Output format style", "suggestions": "Emoji bulleted, Numbered list, Paragraphs"},
	"keywords": {"help": "SEO Keywords", "suggestions": "health, technology, cooking"},
	"reading_level": {"help": "Target reading level", "suggestions": "3rd grade, 6th grade, 9th grade"}
}
