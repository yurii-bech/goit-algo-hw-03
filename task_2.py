import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Запитуємо в користувача рівень рекурсії
    order = int(input("Введіть рівень рекурсії (ціле число більше нуля): "))

    # Ініціалізуємо модуль Turtle
    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()

    # Налаштовуємо початкове положення та орієнтацію
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-150, 90)
    my_turtle.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(my_turtle, order, 300)
        my_turtle.right(120)

    # Закриваємо Turtle
    my_screen.mainloop()

if __name__ == "__main__":
    main()