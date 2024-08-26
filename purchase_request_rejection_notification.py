from abstra.workflows import *
from abstra.tables import *
from abstra.connectors import get_access_token
import slack_sdk as slack
from slack_sdk.errors import SlackApiError

slack_token = get_access_token("slack").token

purchase_data = get_data("purchase_data")
requester_team_email = purchase_data["requester_intern_email"]

reject_message = get_data("rejection_reason")
assignee_emails = get_data("assignee_emails")


def slack_msg(message, channel, token):
    client = slack.WebClient(token=token)
    try:
        client.chat_postMessage(
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


# notify the requester on slack about the rejection
user_id = get_slack_ids_from_email(slack_token, requester_team_email)
message = f"Your purchase request has been declined for the following reason(s): {reject_message}. \nPlease contact the finance team for further assistance."

slack_msg(message, user_id, slack_token)
