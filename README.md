# Purchase Request Workflow Template

Leverage Abstra Workflows to streamline and customize your employee registration processes.

This functional template includes the following steps:

- An onboarding form to collect purchase requests.
- Depending on the value, the request is either automatically approved or sent via email to the responsible team for approval.
- Finally, an overview of the order is sent on Slack to the requester, informing them about the status.

![A purchase request approval/rejection worklow built in Abstra](https://github.com/user-attachments/assets/979e1ecb-4a64-49ce-8105-8899303cb85e)

This template integrates with Slack. To make these integrations work, you must add your own API Keys for these services.

API Keys required:

- `SLACK_BOT_TOKEN`

## Table Schema:
`payables`:
|updated_at|description|amount|purchase_request_id|
|:-:|:-:|:-:|:-:|
|```timestamp```|```str```|```int```|```str```|

`purchase_request_approvals`:
|approved|purchase_request_id|team_id|
|:-:|:-:|:-:|
|```bool```|```str```|```str```|

`purchase_requests`:
|id|created_at|
|:-:|:-:|
|```str```|```timestamp```|

`team`:
|name|intern_email|position|
|:-:|:-:|:-:|
|```str```|```str```|```str```|

If you're interested in customizing this template for your team in under 30 minutes, [book a customization session here.](https://meet.abstra.app/sophia-solo?url=github-template-credit-onboarding)
