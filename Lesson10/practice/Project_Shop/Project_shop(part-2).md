# Проект: Управление инвентарем в интернет-магазине (Часть 2)

## Описание

Расширить консольное приложение для управления инвентарем интернет-магазина, добавив уникальные идентификаторы для товаров и изменив логику работы пунктов меню. Приложение должно обеспечивать выполнение следующих операций:

* **Добавление товара:**
    * Пользователь вводит название товара, цену и количество.
    * Каждому товару присваивается уникальный идентификатор.
    * Товар добавляется в систему.
* **Удаление товара:**
    * Пользователь вводит идентификатор товара.
    * Товар удаляется из системы.
* **Обновление товара:**
    * Пользователь вводит идентификатор товара.
    * Пользователь выбирает, какое поле необходимо обновить (название, цена, количество).
    * Пользователь вводит новое значение для выбранного поля.
* **Поиск товара по названию:**
    * Пользователь вводит часть названия товара.
    * Система выводит список товаров, названия которых содержат введенную подстроку.
* **Вывод списка всех товаров:**
    * Система выводит список всех товаров в формате: "id: [id], Название: [название], Цена: [цена], Количество: [количество]".
* **Вывод товаров с ценой ниже заданной:**
    * Пользователь вводит значение цены.
    * Система выводит список товаров, цена которых ниже введенного значения.
* **Вывод товаров с количеством ниже заданного:**
    * Пользователь вводит значение количества.
    * Система выводит список товаров, количество которых ниже введенного значения.


# Принципы работы ID в системе управления инвентарем

## 1. Уникальность

* Каждый товар в системе должен иметь уникальный идентификатор (ID).
* ID не должен повторяться для разных товаров.
* Уникальность ID гарантирует, что каждый товар может быть однозначно идентифицирован.

## 2. Неизменность

* ID товара должен быть неизменным на протяжении всего времени его существования в системе.
* После присвоения ID товару он не должен меняться.
* Неизменность ID обеспечивает стабильность и надежность системы.

## 3. Простота

* ID должен быть простым и удобным для использования.
* Рекомендуется использовать целочисленные ID, так как они легко обрабатываются и сравниваются.

## 4. Автоматическая генерация

* ID должен генерироваться автоматически при добавлении нового товара в систему.
* Автоматическая генерация ID исключает возможность дублирования и ошибок, связанных с ручным вводом.
* Можно использовать автоинкрементный подход, где ID каждого нового товара на 1 больше ID предыдущего добавленного товара.

## 5. Использование ID для операций

* ID должен использоваться для выполнения операций с товарами, таких как удаление, обновление и поиск.
* Использование ID упрощает выполнение операций и делает систему более надежной.
* При выводе списка товаров ID каждого товара должен быть включен в отображаемую информацию.

## 6. Обработка ошибок

* Система должна обрабатывать ошибки, связанные с некорректным использованием ID.
* Если пользователь вводит несуществующий ID при выполнении операции, система должна выдавать сообщение об ошибке.
* Обработка ошибок обеспечивает надежность и устойчивость системы.
