import numpy as np
from tqdm import tqdm


class Library:
    def __init__(self, nbooks, signup_time, ship_time, book_list):
        self.nbooks = nbooks
        self.signup_dur = signup_time
        self.ship_rate = ship_time
        self.bookids = book_list


def get_score(lib, scanned_books, signed_libraries, book_score, remaining_days):
    if lib in signed_libraries:
        return -1.0, []

    days_avail = remaining_days - lib.signup_dur
    sorted_books = sorted(lib.bookids - scanned_books, key=lambda b : book_score[b], reverse=True)
    possible_books = sorted_books[:days_avail*lib.ship_rate]
    score = sum(map(book_score.__getitem__, possible_books))
    possible_score = score/lib.signup_dur

    return possible_score, possible_books


if __name__ == "__main__":

    total_books, total_lib, scan_period = map(int, input().split())
    book_points = list(map(int, input().split()))

    libraries = []
    for _ in range(total_lib):
        nbook, signup_dur, ship_rate = map(int, input().split())
        book_ids = set(map(int, input().split()))
        libraries.append(Library(nbook, signup_dur, ship_rate, book_ids))

    curr_day = 0
    assigned_books = set()
    assigned_libraries = set()

    ans_lib = []
    ans_books = []

    for _ in tqdm(range(total_lib)):

        lib_scores, pos_books = map(list, zip(*[get_score(x, assigned_books, assigned_libraries,
                                                          book_points, scan_period-curr_day)
                                                for x in libraries]))
        best_lib = np.argmax(lib_scores)
        best_books = pos_books[best_lib]

        if best_lib in assigned_libraries:
            break

        curr_day += libraries[best_lib].signup_dur
        if curr_day >= scan_period:
            break

        ans_lib.append(best_lib)
        ans_books.append(best_books)

        assigned_books.update(best_books)
        assigned_libraries.add(libraries[best_lib])

    # Output
    print(len(ans_lib))
    for i, lib in enumerate(ans_lib):
        print(f"{lib} {len(ans_books[i])}")
        print(*ans_books[i])






