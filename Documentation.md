`Примечание : для использования API начинайте запрос с /api/`

**Регистрация**
----

* **URL**

  /register/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   
   `password=[string]`
   
   `email=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'username' : 'string', 'password' : "hash_password , 'email' : 'string'}`
    
**Используйте ключ 'access' для авторизации**
 _____
 **Авторизация**
----

* **URL**

  /login/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'refresh' : 'string', 'access' : "string" }`
    
**Используйте ключ 'access' для авторизации**
 _____
 **Создание/Изменение/Удаление цепочек ДНК**
______

* **URL**
  * Для создания

    /create/
  
  * Для изменения
  
    /edit/pk/
  
  * Для удаления

    /delete/pk/
  
  PK - номер цепочки ДНК
  
* **Cоздание**
  * **Метод:**

      `POST`
      
  * **Параметры** 
   
      **Обязательно**
      
      `chain=[string]`
 


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'chain' : "string" }`
    
* **Изменение**
  
    * **Метод**
        
        `PUT`
        
    * **Параметры** 
   
      **Обязательно**
      
      `chain=[string]`
     


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'chain' : "string" }`

* **Удаление**
  
    * **Метод**
        
        `DELETE`
        
    * **Параметры** 
   
      **Обязательно**
      
      `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{}`
______
**Проверка : существует ли кодон в цепочке**
----

* **URL**

  /check/codon/
  
  codon - комбинация из нуклеотидов

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'chain' : "string" }`
    
  * Примечание : находит первую цепочку ДНК с данным кодоном 
    
 _____
