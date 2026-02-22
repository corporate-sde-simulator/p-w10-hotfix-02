# ============================================================
# HOTFIX — DATA-211: /api/users/:id Returns 500 on Missing User
# Priority: P1 | SLA: 30 minutes | Reporter: Frontend Team
# ============================================================
#
# The API endpoint crashes with a 500 error when requesting a user
# that doesn't exist. Should return 404 with a helpful message.
#
# Two bugs:
# ============================================================

class UserService:
    def __init__(self):
        self.users = {
            1: {'id': 1, 'name': 'Alice', 'email': 'alice@test.com'},
            2: {'id': 2, 'name': 'Bob', 'email': 'bob@test.com'},
        }

    def get_user(self, user_id):
        return self.users.get(user_id)  # Returns None if not found


def handle_get_user(user_id):
    service = UserService()
    user = service.get_user(user_id)

    # with TypeError: 'NoneType' object is not subscriptable
    response = {
        'name': user['name'],
        'email': user['email'],
    }

    return {'data': response, 'status': 200}


if __name__ == '__main__':
    print(handle_get_user(1))   # Works
    print(handle_get_user(999)) # Crashes with TypeError!
