# token = vk1.a.mQVtZJdKYVyvXJ24jXrcR3-ZzMJTOezO6HK5sEYQUC66Sd3_fA1dV-q5mQlDms85crdXciS60mptlT-6BeYkmV_u4lZVD6iYHqFErnbNHsWJaTSB6lJIVkuW_tz8EKbKDAJqWtWCz3mKZWIG-JqJYkJgqM2oMcBChfadEm2ayf1x-kaYfs0bzxvivnXB1SjyDF0IHiNbU5iybMCRdHJCGg
# group token='vk1.a.cMRkTWOKd2mIrHRBV0nlM6yB0Dr0pI-qJva2GWrHqrDyy1DI8hsbzrvrRJ-NXdt0OPjzVDVyyu77ms9fdx8tY3oYi7mlfVK_JEcXGizeNO0RfDN6l3vhZA6mzSXJtjQUiBfxalz0u1Ea6RWkT0nzbdXCU5HO66Ldfr6faDmO5QL2Na2wcWrWW8e2m1Hj4iAonXnM44Uy1fn-mKuLW8Y2fw')
# vk1.a.PGOkixVl-YKCBr0RgG-Sk-uNl0q3qjwxXja6N5bzpGwATzPv9HXGyWc7-z8fDQaAaaspkJ-9vipBmgAq1doqhP75PQliqBFQfQjKRIVMu_UHA60oLMHq3Z2oG8WyZLfHx6cR3g3vcFKig-cTPyvealtRpGUSG2Aqv7oVpHZ3zoaNEX55DaWDpC_4OkhWczF6ob2akMH335Y66yfgUryj3w
import asyncio
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api.longpoll
import logging
import multiprocessing
from vk_api.longpoll import VkLongPoll
myuser_id = 578651553
mygroup_id = 229734873
chatId = 210531192
#     vk_session = vk_api.VkApi(token='vk1.a.ThrLrzGLTzpidn4f541Pt2OJxp6ak5ByfcBZ6TCkHIEpVxRQl6GqNOWte4N_-NZJeW60bkye-EaRxhhg69mryaAAUB3o8KtYJICaFngaOxGavSQO2JVVdohLMW8yCVW5UAgQY5kY26-SC2dRufWTgL_dIW_uZ9JmAnf2thF6lk-MycC9fI9_q9m_XAbjWfqZsECQIVnDtPlSmYosxsD_Xg')
#     longpoll_server = VkLongPoll(vk_session, mode= 64)
#     for event in VkLongPoll(vk_session, mode= 64).listen():
#         try:
#             if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#                 user_id = event.group_id
#                 if user_id == chatId:
#                     msg = event.message
#                     print(msg)
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")
# except vk_api.exceptions.ApiError as e:
#     print(f"Ошибка API: {e}")
# except vk_api.exceptions.AuthError as e:
#     print(f"Ошибка авторизации: {e}")

logging.basicConfig(level=logging.INFO)

def listen_vk_updates(queue):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    vk_session = vk_api.VkApi(token="vk1.a.ThrLrzGLTzpidn4f541Pt2OJxp6ak5ByfcBZ6TCkHIEpVxRQl6GqNOWte4N_-NZJeW60bkye-EaRxhhg69mryaAAUB3o8KtYJICaFngaOxGavSQO2JVVdohLMW8yCVW5UAgQY5kY26-SC2dRufWTgL_dIW_uZ9JmAnf2thF6lk-MycC9fI9_q9m_XAbjWfqZsECQIVnDtPlSmYosxsD_Xg")
    for event in VkLongPoll(vk_session, mode= 64).listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.group_id
            if user_id == chatId:
                msg = event.text.strip()
                logging.info(f"Новое сообщение от пользователя {user_id}: {msg}")
                try:
                    queue.put(msg)  # Добавляем сообщение в очередь
                    logging.info(f"Сообщение добавлено в очередь: {msg}")
                except Exception as e:
                    logging.error(f"Ошибка при добавлении сообщения в очередь: {e}")
                