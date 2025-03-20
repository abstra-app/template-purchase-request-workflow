from abstra.compat import use_legacy_threads
"""
Calling the use_legacy_threads function allows using
the legacy threads in versions > 3.0.0
https://abstra.io/docs/guides/use-legacy-threads/

The new way of using workflows is with tasks. Learn more
at https://abstra.io/docs/concepts/tasks/ and contact us
on any issues during your migration
"""
use_legacy_threads("scripts")

from abstra.workflows import *
from abstra.tables import *
from abstra.connectors import get_access_token
import os
import slack_sdk as slack
from slack_sdk.errors import SlackApiError

slack_token = get_access_token("slack").token

purchase_data = get_data("purchase_data")
requester_team_email = purchase_data["requester_intern_email"]
purchase_request_id = purchase_data["purchase_request_id"]
requester_team_id = purchase_data["requester_team_id"]
description = purchase_data["description"]
amount = purchase_data["amount"]
quantity = purchase_data["quantity"]
reason = purchase_data["reason"]
deadline = purchase_data["deadline"]


def slack_msg(message, channel, token):
    client = slack.WebClient(token=token)
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
    except SlackApiError as e:
        assert e.response["error"]


def get_slack_ids_from_email(token, email):
    client = slack.WebClient(token=token)

    user = client.users_lookupByEmail(
        token=slack_token, email=email)['user']['id']

    return user


user_id = get_slack_ids_from_email(slack_token, requester_team_email)
message = f"Great news!\nYour purchase request for '{description}' has been approved :white_check_mark: \nWe've now forwarded your request to the finance team for additional processing."

slack_msg(message, user_id, slack_token)

# add on payables
amount = 100*purchase_data["amount"]
insert("payables", {"purchase_request_id": purchase_request_id,
                    "amount": amount, "description": purchase_data["description"]})

# notify the finance team on slack
channel = os.getenv("SLACK_CHANNEL_NAME")

finance_message = f":pencil2: New purchase request approved and added to payables. \n\nPurchase Information \n - Description: {description} \n - Amount: R$ {amount/100} \n - Quantity: {quantity} \n - Purchase Deadline: {deadline} \n\nPlease review the request and process payment."
slack_msg(finance_message, channel, slack_token)
