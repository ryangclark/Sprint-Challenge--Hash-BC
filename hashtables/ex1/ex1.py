#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    # (6, 2)

    for i, weight in enumerate(weights):
        partner = limit - weight
        partner_index = hash_table_retrieve(ht, partner)

        if partner_index is not None:
            if (i > partner_index):
                return (i, partner_index)
            else:
                return (partner_index, i)
        else:
            hash_table_insert(ht, weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# print(get_indices_of_item_weights([4, 4], 2, 8))