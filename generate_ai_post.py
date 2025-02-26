#!/usr/bin/env python3
import os
import openai

# Load the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic):
    # Create an SEO keyword from the topic (lowercase, hyphen-separated)
    seo_keyword = topic.replace(" ", "-").lower()

    prompt = f"""
You are a highly skilled **SEO copywriter, web design expert, and digital marketing strategist**. Write a **detailed, engaging, and SEO-optimized** blog post of **950-1050 words** about "{topic}" for the website **www.webdesignnerd.com**.

## Requirements:

### **1. Title & Structure**
   - Start with a **keyword-optimized title** relevant to "{topic}".
   - Use **clear, structured subheadings** (H2 and H3) for readability.
   - **No unnecessary symbols** (e.g., `#`, `*`, or any other markdown symbols).

### **2. SEO Optimization**
   - Include an **SEO-friendly slug**, **meta title**, and **meta description** optimized for search rankings.
   - Naturally mention **www.webdesignnerd.com** throughout the article.
   - Ensure **keyword density is balanced**.
   - Use **internal linking** when relevant.
   - Maintain **readability and natural flow**.

### **3. Content Quality & Readability**
   - Cover a **trending, up-to-date topic** within web design, digital marketing, or SEO.
   - Ensure content is **engaging, informative, and structured** for easy scanning.
   - Use **bullet points, numbered lists, or bold highlights** for important points.
   - Maintain **professionalism, clarity, and grammatical accuracy**.

### **4. AI-Generated Images (Auto-Selected by AI)**
   - Automatically generate and **embed relevant AI-generated images** throughout the post.
   - Each image must match the section’s content and **enhance readability**.
   - The image filenames must reflect the SEO keyword. Format images using:  
     **`[Image: "Generated - {seo_keyword}-image1.jpg"]`**

### **5. Call-to-Action (CTA)**
   - End with a **strong, persuasive CTA** encouraging readers to take action (e.g., sign up, purchase a service, or contact www.webdesignnerd.com).

## **Covered Topics (Rotate Per Post):**
Each post should cover a **unique** topic related to web design, SEO, digital marketing, and e-commerce. (A list of topics follows for reference.)

The **goal** is to generate **high-quality, search-optimized blog content** that attracts organic traffic to **www.webdesignnerd.com** and converts readers into customers.

Ensure the final output is **fully formatted, visually structured, and SEO-ready**, with AI-generated images **automatically embedded**.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()

def main(topic):
    blog_content = generate_post(topic)
    with open("blog_post.txt", "w", encoding="utf-8") as f:
        f.write(blog_content)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python generate_ai_post.py 'Your Topic'")
        sys.exit(1)
    main(sys.argv[1])