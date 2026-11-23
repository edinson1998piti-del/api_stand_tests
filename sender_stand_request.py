import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

if __name__ == "__main__":
    response_new_user = post_new_user(data.user_body)
    response_users_table = get_users_table()
    print(response_new_user.status_code)
    print(response_new_user.json())
    print(response_users_table.status_code)
    print(response_users_table.json())
