"""
DEVUP AI — Multi-Agent Workflow with AutoGen
=============================================
Build powerful AI agent pipelines using Microsoft AutoGen + DEVUP AI.

Install:
    pip install pyautogen openai

Usage:
    export DEVUPAI_API_KEY="dvup_your_key_here"
    python agent.py
"""

import os
import autogen

# ── DEVUP AI config for AutoGen ───────────────────────────────────────────────
DEVUPAI_CONFIG = {
    "config_list": [
        {
            "model": "meta-llama/Llama-3.3-70B-Instruct",
            "api_key": os.environ.get("DEVUPAI_API_KEY"),
            "base_url": "https://api.devupai.com/v1",
        }
    ],
    "temperature": 0.3,
    "max_tokens": 2048,
    "cache_seed": None,  # Disable caching for fresh responses
}

CODER_CONFIG = {
    "config_list": [
        {
            "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
            "api_key": os.environ.get("DEVUPAI_API_KEY"),
            "base_url": "https://api.devupai.com/v1",
        }
    ],
    "temperature": 0.1,  # Low temperature for deterministic code
    "max_tokens": 4096,
    "cache_seed": None,
}


def run_code_review_pipeline(code: str, language: str = "Python") -> None:
    """
    Two-agent pipeline:
    1. Coder agent: reviews the code and suggests improvements
    2. Critic agent: validates the improvements and gives final verdict
    """
    print(f"\n{'='*60}")
    print("🤖 DEVUP AI Multi-Agent Code Review Pipeline")
    print(f"{'='*60}\n")

    # Agent 1: Senior Developer — reviews and improves code
    senior_dev = autogen.AssistantAgent(
        name="SeniorDeveloper",
        llm_config=CODER_CONFIG,
        system_message="""You are a senior software engineer with 10+ years of experience.
        
Your job is to:
1. Review the provided code for bugs, security issues, and performance problems
2. Suggest concrete improvements with code examples
3. Rate the code quality (1-10) with justification

Be specific, practical, and constructive. Focus on the most impactful changes.""",
    )

    # Agent 2: Security Auditor — focuses on security
    security_auditor = autogen.AssistantAgent(
        name="SecurityAuditor",
        llm_config=DEVUPAI_CONFIG,
        system_message="""You are a cybersecurity expert specializing in secure code review.

Your job is to:
1. Identify security vulnerabilities in the code (injection, auth bypass, data leaks, etc.)
2. Assign CVSS severity scores to each issue
3. Provide secure alternatives for each vulnerability found

Use OWASP guidelines. Be thorough but concise.""",
    )

    # Human proxy — orchestrates the conversation
    user_proxy = autogen.UserProxyAgent(
        name="UserProxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
        code_execution_config=False,
        is_termination_msg=lambda msg: "REVIEW_COMPLETE" in msg.get("content", ""),
    )

    # Start the review pipeline
    task = f"""Please review this {language} code:

```{language.lower()}
{code}
```

SeniorDeveloper: Start with a code quality review and improvements.
SecurityAuditor: Follow with a security audit.
End your final message with 'REVIEW_COMPLETE'."""

    user_proxy.initiate_chat(
        recipient=senior_dev,
        message=task,
        max_turns=4,
    )


def run_research_agent(topic: str) -> None:
    """
    Single agent with tool use for research tasks.
    Demonstrates function calling with DEVUP AI.
    """
    print(f"\n{'='*60}")
    print(f"🔍 Research Agent — Topic: {topic}")
    print(f"{'='*60}\n")

    researcher = autogen.AssistantAgent(
        name="Researcher",
        llm_config=DEVUPAI_CONFIG,
        system_message="""You are a research analyst. When given a topic:
1. Provide a structured analysis with key points
2. List pros and cons if applicable
3. Give a practical recommendation
4. End with 'RESEARCH_COMPLETE'""",
    )

    user_proxy = autogen.UserProxyAgent(
        name="UserProxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        code_execution_config=False,
        is_termination_msg=lambda msg: "RESEARCH_COMPLETE" in msg.get("content", ""),
    )

    user_proxy.initiate_chat(
        recipient=researcher,
        message=f"Research this topic and provide a structured analysis: {topic}",
        max_turns=2,
    )


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example 1: Code review pipeline
    sample_code = """
import sqlite3

def get_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def login(username, password):
    user = get_user(username, password)
    if user:
        print(f"Welcome {username}!")
        return True
    return False
"""
    run_code_review_pipeline(sample_code, "Python")

    # Example 2: Research agent
    run_research_agent(
        "Best practices for building AI-powered SaaS products in 2025"
    )
