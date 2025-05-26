from smolagents import PromptTemplates, PlanningPromptTemplate, ManagedAgentPromptTemplate, FinalAnswerPromptTemplate


EMPTY_PROMPT_TEMPLATES = PromptTemplates(
    system_prompt="",
    planning=PlanningPromptTemplate(
        initial_plan="",
        update_plan_pre_messages="",
        update_plan_post_messages="",
    ),
    managed_agent=ManagedAgentPromptTemplate(task="", report=""),
    final_answer=FinalAnswerPromptTemplate(pre_messages="", post_messages=""),
)


DEFAULT_CODE_PROMPT_TEMPLATE = PromptTemplates(
    system_prompt="You're a helpful assistant with a list of tools that are functions that"
                  "you must write code to call. Only choose one tool at a time.",
    planning=PlanningPromptTemplate(
        initial_plan="I will choose the tool best suited for the user's task. Once chosen I only need to write code that calls it. Such as:\nresult = tool(args)",
        update_plan_pre_messages="",
        update_plan_post_messages="",
    ),
    managed_agent=ManagedAgentPromptTemplate(task="", report=""),
    final_answer=FinalAnswerPromptTemplate(pre_messages="", post_messages=""),
)
