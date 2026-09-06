> For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits.md).

# Top up Gateway credits

When your [Gateway credits](/deploy/use-n8n-cloud/gateway-credits.md) balance runs low, top it up from the Cloud admin dashboard. You can add credit manually whenever you need it, or turn on auto top-up so n8n refills your balance for you.

Only the instance owner can top up, and topping up requires an active paid subscription. Free trials include Gateway credits, but not top-ups: if you use up your free credit during a trial, upgrade to a paid plan to add more.

## Top up manually

1. Open the [Cloud admin dashboard](/deploy/use-n8n-cloud/use-the-admin-dashboard.md) and select the **Gateway credits** tab.
2. Select **Top up**.
3. Choose an amount and complete the checkout. You can pay with the payment method saved on your subscription or with a different one. n8n emails you an invoice.

Your new balance appears on the page once the payment completes.

## Set up auto top-up

Auto top-up refills your balance whenever it drops below a threshold you set, keeping it above zero so workflows that rely on Gateway credits keep running. Unlike manual top-ups, auto top-up always charges the payment method saved on your subscription.

1. Open the [Cloud admin dashboard](/deploy/use-n8n-cloud/use-the-admin-dashboard.md) and select the **Gateway credits** tab.
2. Turn on **Auto top-up**.
3. Set **When balance drops to** (the balance that triggers a top-up) and **Top up to** (the balance to refill to).
4. Optionally, turn on **Monthly auto top-up limit** to cap how much auto top-up can add per month.
5. Select **Save changes**.

{% hint style="info" %}
If your balance is already below the threshold when you save, n8n triggers a one-time top-up straight away to reach your target balance. The page shows the estimated cost before you save.
{% endhint %}

How auto top-up behaves:

* n8n emails you an invoice each time auto top-up adds credit.
* If you set a monthly limit, auto top-up pauses once it adds that amount in the current month, and resumes the next month.
* If a payment fails, n8n retries. If the retries also fail, n8n turns auto top-up off and emails you. Because auto top-up always charges the payment method saved on your subscription, fix that payment method before turning it back on.

## Overspend

Your balance can run out in the middle of an execution. When that happens, n8n lets the in-flight Gateway requests finish rather than stopping them partway through, so your balance can dip slightly below zero. n8n deducts the overspent amount from your next top-up, and the deduction appears in your [top-up history](/deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md#top-up-history).

## Refunds

Top-ups are final. n8n doesn't refund unused credits except where required by law. If you think a charge is wrong, [contact n8n support](https://www.n8n.io/contact). For expiry and forfeiture rules, refer to [Credit expiry and forfeiture](/deploy/use-n8n-cloud/gateway-credits.md#credit-expiry-and-forfeiture).

## Related resources

* [Gateway credits](/deploy/use-n8n-cloud/gateway-credits.md): how Gateway credits work.
* [Track Gateway credit spend](/deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md): monitor your balance, spend, and top-up history.
* [Service pricing page](https://app.n8n.cloud/service-pricing): current rates for all supported services and models.
