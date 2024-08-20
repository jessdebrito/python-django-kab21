from database.services import *

print(creat_user('Daniel', '1234567', 'senhadificil'))
# print(users)
# print(get_all_users())
# print(get_user_by_id(2))
# print(delete_user_by_id(1))
print(update_user(1, username='Filipe', password='99999999'))