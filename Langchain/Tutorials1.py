ChatModels
Chat models are often backed by LLMs but tuned specifically for having conversations. Crucially, their provider APIs use a 
different interface than pure text completion models. Instead of a single string, they take a list of chat messages as input 
and they return an AI message as output.

LLM
LLMs in LangChain refer to pure text completion models.
Language models that takes a string as input and returns a string. 
LangChain does not host any LLMs, rather we rely on third party integrations.

Effective Prompting Strategies: 
Zero-Shot Prompting: Directly ask the task.
One-Shot Prompting: Provide one example before the task.
Few-Shot Prompting: Provide a few examples.
Chain-of-Thought Prompting: Include intermediate steps.
Instruction Prompting: Give explicit instructions.
Role-Playing Prompting: Assign a role or persona.
Contextual Prompting: Provide additional context.
Interactive Prompting: Engage in a conversational manner.

Messages:
Some language models take a list of messages as input and return a message. 

Some language models take a list of messages as input and return a message. There are a few different types of messages. 
All messages have a role, content, and response_metadata property.

The role describes WHO is saying the message. LangChain has different message classes for different roles.

The content property describes the content of the message. This can be a few different things:

A string (most models deal this type of content)
A List of dictionaries (this is used for multimodal input, where the dictionary contains information about that input type and that input location)


* `ps -ef`: This command shows all running processes with detailed information, including the process ID, parent process ID, and command line.
* `|`: This is a pipe symbol that takes the output of the first command and sends it as input to the second command.
* `grep ollama`: This command searches the output of the previous command for any lines that contain the string "ollama".

Unnormalized Output:

Logits are the direct outputs from the final layer of the neural network.
They are not probabilities but can be converted into probabilities using an activation function like softmax.
Confidence Scores:

The magnitude of a logit indicates the model's confidence in the corresponding prediction.
A higher logit for a particular token or class means the model is more confident that this is the correct prediction.
    
    Tokenization:

The question is tokenized into numerical IDs.
For example, "Who is the prime minister of India?" might be tokenized into a sequence of IDs: [101, 2054, 2003, 1996, 3051, 2801, 1997, 2637, 1029].
Generating the Next Token:

The model processes the input token IDs and generates logits for the next token.
Let's say the logits for the next token (simplified) are: [0.5, 2.3, -1.0, 0.7, 1.5].
Selecting the Next Token:

The token with the highest logit is selected as the next token.
In this case, the token corresponding to the logit 2.3 is selected.
Suppose this token ID corresponds to the word "Narendra"
