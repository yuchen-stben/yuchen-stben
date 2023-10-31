import autogen
# from config import config_list

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        # "model": ["gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
        "model": ["gpt-4-32k", "gpt-4", "gpt-35-turbo"],

    },
)
llm_config ={
        "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0.5,  # temperature for sampling
    }

# create an AssistantAgent named "assistant"
affirmativeSpeaker_1 = autogen.AssistantAgent(
    name="Mbappe",
    system_message="You're the first defence, you are a professional football player, you can suggest opinions that are convincing",
    llm_config=llm_config,  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)
affirmativeSpeaker_2 = autogen.AssistantAgent(
    name="Yang_YC",
    system_message="You are a TEENAGER as the second defence, you think Gou_Qinghua doesn't know much about football and has an unconvincing point of view",
    llm_config=llm_config,  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

negativeSpeaker_1 = autogen.AssistantAgent(
    name="Gou_Qinghua",
    system_message="You, as a contrarian, you don't know much about football and often confuse footballers with NBA players, and you acknowledge that fact",
 # configuration for autogen's enhanced inference API which is compatible with OpenAI API
    llm_config=llm_config,  # configuration for autogen's enhanced inference API which is compatible with OpenAI API

)

negativeSpeaker_2 = autogen.AssistantAgent(
    name="Rui_Yang",
    system_message="You're the second defence",
 # configuration for autogen's enhanced inference API which is compatible with OpenAI API
    llm_config=llm_config,  # configuration for autogen's enhanced inference API which is compatible with OpenAI API

)

debateModerator = autogen.AssistantAgent(
    name ="Moderator",
    llm_config=llm_config,
    system_message='You, as the debate moderator, preside over the debate (Note that both sides only have a first and second defence, not a third and fourth defence. The order of the debate Forward first defence, reverse first defence, forward second defence, reverse second defence, then Debate_judge sums up, declares the end of the debate and replies to the TERMINATE）',
    )

debateJudge = autogen.AssistantAgent(
    name="Debate_judge",
    llm_config=llm_config,
    system_message="Pointing out the performance of the debaters and deciding who wins between the pro and con side"
)


# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False
)

debate_goup_chat = autogen.GroupChat(agents=[affirmativeSpeaker_1,affirmativeSpeaker_2,negativeSpeaker_1,negativeSpeaker_2,debateModerator],
                                     messages=[],max_round=10,)    

group_caht_mgr = autogen.GroupChatManager(groupchat=debate_goup_chat,
                                          llm_config=llm_config,
                                          max_consecutive_auto_reply=10,
                                          human_input_mode='NEVER',)
# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    # affirmativeSpeaker,
    # negativeSpeaker,
    group_caht_mgr,
    message="""Topic of discussion：Ronaldo is better than Messi""",
)
