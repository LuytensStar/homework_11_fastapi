Проект на fastapi що створює таблицю Contact в Postgresql , кожний користувач має імя, прізвище, електронну адресу, номер телефону,день народження і додаткову інформацію.Всі поля за виключенням додаткової інформації 
є обов'язковими
Маршрути:



GET
/api/contacts/
Отримати список всіх контактів


POST
/api/contacts/
Створити контакт


GET
/api/contacts/{contact_id}
Отримати конкретний контакт за contact_id


PUT
/api/contacts/{contact_id}
Оновити контакт з contact_id


DELETE
/api/contacts/{contact_id}
Видалити контакт за contact_id


GET
/api/contacts/search/?query=
Знайти контакт за співпадінням в імені, прізвищі чи електронній пошті


GET
/api/contacts/birthdays/
Отримати список контактів на найближчі 7 днів
