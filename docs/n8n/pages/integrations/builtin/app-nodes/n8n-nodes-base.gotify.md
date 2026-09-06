> For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify.md).

# Gotify

Use the Gotify node to automate work in Gotify, and integrate Gotify with other applications. n8n has built-in support for a wide range of Gotify features, including creating, deleting, and getting messages.

On this page, you'll find a list of operations the Gotify node supports and links to more resources.

{% hint style="info" %}
**Credentials**

Refer to [Gotify credentials](/integrations/builtin/credentials/gotify.md) for guidance on setting up authentication.
{% endhint %}

{% hint style="info" %}
**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](/build/integrate-ai/ai-examples/use-ai-for-parameters.md).
{% endhint %}

## Operations <a href="#operations" id="operations"></a>

* Message
  * Create
  * Delete
  * Get All

## Create message

When creating a message, you can configure the following:

### Additional fields

* **Priority**: The priority of the message (default: 1)
* **Title**: The title of the message

### Options

* **Content Type**: The message content type. Choose between:
  * **Plain**: The message renders as plain text (default)
  * **Markdown**: The message renders as markdown
* **Click URL**: Opens this URL when you click the notification
* **Big Image URL**: Shows a big image in the notification
* **Intent URL**: Opens an intent URL after the notification is delivered (Android only)

/// note | Message extras The **Options** fields (**Click URL**, **Big Image URL**, **Intent URL**) use Gotify's message extras feature. These allow you to customize how notifications are displayed and behave in Gotify clients. Refer to [Gotify's message extras documentation](https://gotify.net/docs/msgextras){:target="\_blank" .external-link} for more details. ///

## Templates and examples

## Templates and examples <a href="#templates-and-examples" id="templates-and-examples"></a>

[Browse Gotify node documentation integration templates](https://n8n.io/integrations/gotify) or [search all templates](https://n8n.io/workflows/)
