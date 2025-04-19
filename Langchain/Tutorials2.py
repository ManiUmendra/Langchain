Message types
ChatModels take a list of messages as input and return a message. There are a few different types of messages. 
All messages have a role and a content property. The role describes WHO is saying the message. LangChain has different message 
classes for different roles. The content property describes the content of the message. 
This can be a few different things:

A string (most models deal this type of content)
A List of dictionaries (this is used for multi-modal input, where the dictionary contains information about that input type and that input location)
In addition, messages have an additional_kwargs property. This is where additional information about messages can be passed.
This is largely used for input parameters that are provider specific and not general. The best known example of this is 
function_call from OpenAI.

HumanMessage
This represents a message from the user. Generally consists only of content.

AIMessage
This represents a message from the model. This may have additional_kwargs in it - for example tool_calls if using
OpenAI tool calling.

SystemMessage
This represents a system message, which tells the model how to behave. This generally only consists of content. Not every model 
supports this.

FunctionMessage
This represents the result of a function call. In addition to role and content, this message has a name parameter which conveys 
the name of the function that was called to produce this result.

ToolMessage
This represents the result of a tool call. This is distinct from a FunctionMessage in order to match OpenAI's function and tool 
message types. In addition to role and content, this message has a tool_call_id parameter which conveys the id of the call to the tool 
that was called to produce this result.



Prompts

Prompts are specific text inputs given to a language model to generate a response. A prompt can be a question, a statement, or any
text that guides the model to produce a desired output. Prompts are typically static and are used directly without any additional 
structure or customization.

Prompt Templates 

These are structured templates that define a reusable pattern for creating prompts. They allow for dynamic insertion of variables
or placeholders, making them more flexible and reusable for different inputs. Prompt templates help standardize the way prompts are 
constructed, ensuring consistency and ease of use across different scenarios.


OUTPUT Paser -------------->>>>>>>>>>>>>>>>>>>>>>

Language models output text. But many times you may want to get more structured information than just text back. 
This is where output parsers come in.

Output parsers are classes that help structure language model responses. There are two main methods an output parser must implement:

"Get format instructions": A method which returns a string containing instructions for how the output of a language model should 
be formatted.

"Parse": A method which takes in a string (assumed to be the response from a language model) and parses it into some structure.
And then one optional one:

"Parse with prompt": A method which takes in a string (assumed to be the response from a language model) and a prompt 
(assumed to be the prompt that generated such a response) and parses it into some structure. The prompt is largely provided
in the event the OutputParser wants to retry or fix the output in some way, and needs information from the prompt to do so.