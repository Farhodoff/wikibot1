from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def recent_books_list(book_data):
    recent_books = InlineKeyboardMarkup(row_width=5)
    inline_buttons = [InlineKeyboardButton(text=f"{i+1}", callback_data=f"id_{book_data[i]['id']}")
                      for i in range(len(book_data))]
    recent_books.add(*inline_buttons)
    return  recent_books


def book_keyboard(url, dowload):
    recent_books_markup = InlineKeyboardMarkup(row_width=1)
    url_button = InlineKeyboardButton(text="Url", url=url)
    dowload_button = InlineKeyboardButton(text="Dowload", url=dowload)

    recent_books_markup.add(url_button, dowload_button)


    return recent_books_markup