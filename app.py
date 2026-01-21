from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    generated = None
    if request.method == "POST":
        ptype = request.form.get("prompt_type")
        topic = request.form.get("topic", "").strip()
        style = request.form.get("style", "").strip()
        detail = request.form.get("detail", "").strip()
        include_sections = request.form.get("include_sections") == "on"

        if not ptype or not topic:
            generated = "⚠️ Please select a prompt type and enter a topic/question."
        else:
            if ptype == "one_line":
                generated = (
                    f"Give a concise, one-line answer to the following question: '{topic}'. "
                    f"Keep it clear, direct, and easy to understand. Style: {style or 'neutral'}."
                )

            elif ptype == "brief":
                if detail == "basic":
                    generated = (
                        f"Write a short, 2-line answer for '{topic}'. "
                        f"Keep it simple, clear, and focused. Style: {style or 'neutral'}."
                    )
                elif detail == "moderate":
                    generated = (
                        f"Write a brief, 4-line explanation for '{topic}'. "
                        f"Include key points with clarity and logical flow. "
                        f"Make it moderately detailed and easy to understand. "
                        f"Style: {style or 'neutral'}."
                    )
                elif detail == "detailed":
                    generated = (
                        f"Write a detailed, 6-line answer for '{topic}'. "
                        f"Begin with a short introduction, then cover all important aspects clearly. "
                        f"Explain concepts in a smooth, organized way using complete sentences. "
                        f"Ensure the explanation is well-structured and coherent. "
                        f"Avoid repetition or filler words, and maintain readability throughout. "
                        f"Style: {style or 'neutral'}."
                    )
                else:
                    generated = f"Write a brief answer for '{topic}'. Style: {style or 'neutral'}. Detail level: {detail or 'moderate'}."

            elif ptype == "pointwise":
                if detail == "basic":
                    generated = (
                        f"Explain '{topic}' in 3 short, clear, numbered points. "
                        f"Keep each point concise and simple. Style: {style or 'neutral'}."
                    )
                elif detail == "moderate":
                    generated = (
                        f"Explain '{topic}' in 5 well-structured, numbered points. "
                        f"Each point should provide meaningful information and flow logically. "
                        f"Keep it moderately detailed and easy to read. "
                        f"Style: {style or 'neutral'}."
                    )
                elif detail == "detailed":
                    generated = (
                        f"Explain '{topic}' in 8 detailed, numbered points. "
                        f"Start with a short introduction before listing the points. "
                        f"Each point should cover one important concept, feature, or example. "
                        f"Ensure clarity, completeness, and proper logical order. "
                        f"Use clear, well-structured sentences for better readability. "
                        f"Style: {style or 'neutral'}."
                    )
                else:
                    generated = f"Explain '{topic}' in clear, numbered points. Style: {style or 'neutral'}. Detail level: {detail or 'moderate'}."

            elif ptype == "pdf":
                sec = "Include sections: Introduction, Main Points, Conclusion." if include_sections else ""
                if detail == "basic":
                    generated = (
                        f"Create a concise, 1-page PDF-ready report about '{topic}'. "
                        f"Keep the content short and clear. {sec}"
                    )
                elif detail == "moderate":
                    generated = (
                        f"Create a moderately detailed, 2-page PDF-ready report about '{topic}'. "
                        f"Cover key points with clear explanations and smooth transitions. "
                        f"Ensure proper flow and professional formatting. {sec}"
                    )
                elif detail == "detailed":
                    generated = (
                        f"Create a comprehensive, 3-page PDF-ready report about '{topic}'. "
                        f"Start with an engaging introduction that defines the topic. "
                        f"Then explain main ideas in depth, using examples or comparisons where suitable. "
                        f"Maintain formal, academic tone and logical section flow. "
                        f"Conclude with a summary of key insights. "
                        f"Ensure the structure is clear, coherent, and visually well-organized. {sec}"
                    )
                else:
                    generated = f"Create a detailed PDF-ready report about '{topic}'. {sec}"

            elif ptype == "doc":
                sec = "Include headings and subheadings." if include_sections else ""
                if detail == "basic":
                    generated = (
                        f"Prepare a concise, 1-page Word (DOCX) document on '{topic}'. "
                        f"Keep the content clear and simple. {sec}"
                    )
                elif detail == "moderate":
                    generated = (
                        f"Prepare a moderately detailed, 2-page Word (DOCX) document on '{topic}'. "
                        f"Explain key points clearly with proper structure and transitions. {sec}"
                    )
                elif detail == "detailed":
                    generated = (
                        f"Prepare a comprehensive, 3-page Word (DOCX) document on '{topic}'. "
                        f"Organize content with appropriate headings, subheadings, and paragraph divisions. "
                        f"Start with an introduction, then develop the main discussion in sections. "
                        f"Use examples, comparisons, and structured explanations to enrich content. "
                        f"End with a brief conclusion summarizing the key insights. "
                        f"Ensure formatting is professional and consistent. {sec}"
                    )
                else:
                    generated = f"Prepare a Word (DOCX) document for '{topic}'. {sec}"

            elif ptype == "ppt":
                sec = "Include slide titles and bullet points for each slide." if include_sections else ""
                if detail == "basic":
                    generated = (
                        f"Create a simple PowerPoint (PPT) outline for '{topic}' with around 5 slides. "
                        f"Keep each slide short and clear. {sec}"
                    )
                elif detail == "moderate":
                    generated = (
                        f"Create a moderately detailed PowerPoint (PPT) outline for '{topic}' with around 8 slides. "
                        f"Each slide should contain meaningful bullet points and concise information. {sec}"
                    )
                elif detail == "detailed":
                    generated = (
                        f"Create a comprehensive PowerPoint (PPT) outline for '{topic}' with around 12 slides. "
                        f"Begin with a title and introduction slide explaining the theme. "
                        f"Follow with content slides arranged logically, covering definitions, examples, and analysis. "
                        f"Ensure bullet points are clear, relevant, and visually balanced per slide. "
                        f"Conclude with a summary or conclusion slide highlighting takeaways. "
                        f"Maintain smooth flow and professional presentation tone. {sec}"
                    )
                else:
                    generated = f"Create a PowerPoint (PPT) outline for '{topic}'. {sec}"

            else:
                generated = "⚠️ Unknown prompt type."
    return render_template("index.html", prompt=generated)

if __name__ == "__main__":
    app.run(debug=True)