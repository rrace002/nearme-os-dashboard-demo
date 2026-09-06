> For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n.md).

# LangChain in n8n

n8n's AI nodes implement [LangChain](https://js.langchain.com/docs/get_started/introduction)'s JavaScript framework. Each node is configurable: choose your own agent, LLM, memory, and other components. You can connect any other n8n node to your LangChain nodes as normal, so you can combine LangChain logic with any other data source or service n8n supports.

This page is for readers who already know LangChain and want to see how its concepts map onto n8n. If you're new to AI concepts, start with [Understand AI components](/build/integrate-ai/understand-ai-components.md) instead.

## How LangChain concepts map to n8n nodes

n8n represents most LangChain concepts as [cluster nodes](/integrations/builtin/cluster-nodes.md): a [root node](/key-concept-glossary.md#root-node-n8n) that defines the cluster's main functionality, with one or more [sub-nodes](/key-concept-glossary.md#sub-node-n8n) attached to extend it.

| LangChain concept | Node category | Example nodes                                                                                                                                                                                                                                                                                                                                        | Learn more                                                                                                               |
| ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Chain             | Root node     | [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md), [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa.md), [Summarization Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md)              | [What's a chain in AI?](/build/integrate-ai/understand-ai-components/what-chains-do.md)                                  |
| Agent             | Root node     | [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md)                                                                                                                                                                                                                                                              | [What's an agent in AI?](/build/integrate-ai/understand-ai-components/what-agents-do.md)                                 |
| Language model    | Sub-node      | [Anthropic Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md), [OpenAI Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai.md), [Ollama Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama.md)                         | [Sub-nodes](/integrations/builtin/cluster-nodes/sub-nodes.md)                                                            |
| Vector store      | Root node     | [Pinecone Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md), [Qdrant Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md), [Simple Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md) | [Store and search data with vectors](/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors.md) |
| Memory            | Sub-node      | [Postgres Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md), [Redis Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md), [Simple Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow.md)                 | [How memory works](/build/integrate-ai/understand-ai-components/how-memory-works.md)                                     |
| Tool              | Sub-node      | [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md), [Custom Code Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md), [Wikipedia](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md)                                      | [What's a tool in AI?](/build/integrate-ai/understand-ai-components/how-tools-work.md)                                   |
| Retriever         | Sub-node      | [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md), [Workflow Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md)                                                                                                                    | [Retrieve relevant context](/build/integrate-ai/understand-ai-components/retrieve-relevant-context.md)                   |
| Embeddings        | Sub-node      | [Embeddings OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md), [Embeddings Cohere](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)                                                                                                                               | [Retrieve relevant context](/build/integrate-ai/understand-ai-components/retrieve-relevant-context.md)                   |
| Document loader   | Sub-node      | [Default Data Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md), [GitHub Document Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)                                                                                                           | [Sub-nodes](/integrations/builtin/cluster-nodes/sub-nodes.md)                                                            |
| Output parser     | Sub-node      | [Structured Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured.md), [Auto-fixing Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md)                                                                                                    | [Sub-nodes](/integrations/builtin/cluster-nodes/sub-nodes.md)                                                            |
| Text splitter     | Sub-node      | [Recursive Character Text Splitter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md), [Token Splitter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md)                                                                               | [Sub-nodes](/integrations/builtin/cluster-nodes/sub-nodes.md)                                                            |

Memory sub-nodes only attach to the [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md) root node. Unlike LangChain, none of n8n's chain nodes support memory, so they can't reference earlier messages in a conversation. If your workflow needs to do that, use an agent instead of a chain.

The examples above aren't exhaustive. For the full, up-to-date list of nodes in each category, browse the [root nodes](/integrations/builtin/cluster-nodes/root-nodes.md) and [sub-nodes](/integrations/builtin/cluster-nodes/sub-nodes.md) libraries. n8n also provides the [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger.md) node to start a workflow from a chat message, and the [LangChain Code](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md) node, which lets you write LangChain JavaScript code directly for functionality that doesn't have a dedicated n8n node yet.

## Use LangSmith with a self-hosted n8n instance

[LangSmith](https://www.langchain.com/langsmith) is a developer platform from the LangChain team. Connect a self-hosted n8n instance to LangSmith to record and monitor n8n executions, the same way you'd trace a LangChain application.

{% hint style="info" %}
**Feature availability**

LangSmith tracing is available on:

* **Self-hosted:** All editions

It isn't available on n8n Cloud.
{% endhint %}

To connect n8n to LangSmith:

1. [Log in to LangSmith](https://smith.langchain.com/settings) and get your API key.
2. Set the following [environment variables](/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables.md) in the environment where you host n8n:

   | Variable                         | Value                                        |
   | -------------------------------- | -------------------------------------------- |
   | `LANGCHAIN_ENDPOINT`             | `https://api.smith.langchain.com`            |
   | `LANGCHAIN_TRACING_V2`           | `true`                                       |
   | `LANGCHAIN_API_KEY`              | Your LangSmith API key                       |
   | `LANGCHAIN_PROJECT`              | Optional project name. Defaults to `default` |
   | `LANGCHAIN_CALLBACKS_BACKGROUND` | `true` to upload traces asynchronously       |
3. Restart n8n.

LangSmith creates a project named **default** after n8n sends its first trace, unless you set `LANGCHAIN_PROJECT` to a different name. Every trace then goes to that project instead. Traces can arrive with a short delay, because `LANGCHAIN_CALLBACKS_BACKGROUND` uploads them asynchronously by default. Set it to `false` for synchronous uploads when you're debugging.

For information on using LangSmith itself, refer to [LangSmith's documentation](https://docs.smith.langchain.com/).

## Learn more about LangChain

You don't need to know LangChain to use n8n, but these resources can help if you want to go deeper:

* The [LangChain documentation](https://docs.langchain.com/docs/) covers key concepts and use cases. Choose [LangChain | Python](https://python.langchain.com/docs/get_started/introduction) or [LangChain | JavaScript](https://js.langchain.com/docs/get_started/introduction/) for quickstarts, code examples, and API documentation. LangChain also provides [code templates](https://github.com/langchain-ai/cookbooks) for Python and JavaScript, with ideas for common patterns and use cases.
* [What's LangChain?](https://www.ibm.com/think/topics/langchain) explains LangChain terminology in plain language, for a general audience.
* This [YouTube series by Greg Kamradt](https://youtu.be/_v_fgW2SkkQ?si=8Z2tfAoXnN3lXU9s) works through the LangChain documentation with code examples.
* Join the n8n [Discord](https://discord.gg/bAt54txhHg) to discuss LangChain and share your projects with the n8n community.
