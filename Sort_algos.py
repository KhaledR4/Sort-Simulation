from constants import *
from Drawings.objects import *
import time
from Drawings.drawings import *


def basic_sort(to_sort):
    DrawLegends.basic_sort()

    for i in range(len(to_sort)):
        # change ith bar to currently working color
        draw_one_bar(to_sort[i], "red")

        time.sleep(0.1)
        for j in range(i+1, len(to_sort)):
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

            # change jth bar to comparison color
            draw_one_bar(to_sort[j], "green")
            time.sleep(0.1)

            # switch bars if we find new minimum
            if to_sort[i].height > to_sort[j].height:
                draw_one_bar(to_sort[i], "white")   # white to avoid collision of colors since i is higher
                to_sort[i].height, to_sort[j].height = to_sort[j].height, to_sort[i].height
                draw_one_bar(to_sort[i], "red")

            # change jth bar back to normal color
            draw_one_bar(to_sort[j], "blue")

        # change ith bas back to normal color
        draw_one_bar(to_sort[i], "blue")


def bubble_sort(to_sort):
    DrawLegends.bubble_sort()

    i = 0
    while i < len(to_sort):
        for j in range(len(to_sort)-1):
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

            draw_one_bar(to_sort[j], "green")
            draw_one_bar(to_sort[j+1], "red")
            time.sleep(0.1)

            if to_sort[j].height > to_sort[j+1].height:
                draw_one_bar(to_sort[j], "white")   # white to avoid collision of colors since i is higher
                to_sort[j].height, to_sort[j+1].height = to_sort[j+1].height, to_sort[j].height
                draw_one_bar(to_sort[j], "green")

            draw_one_bar(to_sort[j], "blue")
            draw_one_bar(to_sort[j + 1], "blue")
        i += 1


def insertion_sort(to_sort, first_call=True):
    if first_call:
        DrawLegends.insertion_sort()

    for i in range(1, len(to_sort)):
        working_index = i
        while working_index > 0:
            draw_one_bar(to_sort[working_index - 1], "green")
            draw_one_bar(to_sort[working_index], "red")
            time.sleep(0.1)
            if to_sort[working_index].height < to_sort[working_index-1].height:
                draw_one_bar(to_sort[working_index - 1], "white")
                to_sort[working_index].height, to_sort[working_index - 1].height = to_sort[working_index-1].height,\
                                                                                   to_sort[working_index].height
                draw_one_bar(to_sort[working_index], "blue")
                draw_one_bar(to_sort[working_index - 1], "blue")
                working_index -= 1
            else:
                draw_one_bar(to_sort[working_index - 1], "blue")
                draw_one_bar(to_sort[working_index], "black")
                time.sleep(0.5)
                draw_one_bar(to_sort[working_index], "blue")
                break


def quick_sort(to_sort, first_call=True):
    if first_call:
        DrawLegends.quick_sort()

    if to_sort:
        i = -1
        draw_one_bar(to_sort[-1], "red")
        pivot = to_sort[-1]
        time.sleep(0.05)
        for j in range(len(to_sort)-1):
            draw_one_bar(to_sort[j], "green")
            time.sleep(0.05)
            if to_sort[j].height > pivot.height:
                draw_one_bar(to_sort[j], "blue")
                continue
            else:
                if i != -1:
                    draw_one_bar(to_sort[i], "blue")
                i += 1
                draw_one_bar(to_sort[i], "black")
                time.sleep(0.05)
                draw_one_bar(to_sort[j], "white")
                draw_one_bar(to_sort[i], "white")
                to_sort[j].height, to_sort[i].height = to_sort[i].height, to_sort[j].height
                draw_one_bar(to_sort[j], "blue")
                draw_one_bar(to_sort[i], "black")
                time.sleep(0.05)

        draw_one_bar(to_sort[i], "blue")
        i += 1
        draw_one_bar(pivot, "white")
        draw_one_bar(to_sort[i], "white")
        pivot.height, to_sort[i].height = to_sort[i].height, pivot.height
        draw_one_bar(pivot, "red")
        draw_one_bar(to_sort[i], "blue")
        draw_one_bar(pivot, "blue")

        if len(to_sort) > 1:
            quick_sort(to_sort[:i], False)
            quick_sort(to_sort[i+1:], False)


def merge(to_sort):
    DrawLegends.merge_sort()
    results = merge_sort(to_sort[:int(len(to_sort) / 2)], to_sort[int(len(to_sort) / 2):], to_sort)
    for i, result in enumerate(results):
        draw_one_bar(result, "white")
        to_sort[i].height = result.height
        draw_one_bar(result, "blue")
        time.sleep(0.1)


def merge_sort(right, left, to_sort):
    if len(right) >= 1 and len(left) >= 1:
        for i in range(int(len(to_sort) / 2)):
            draw_one_bar(to_sort[i], "red")
        for i in range(int(len(to_sort)/2), len(to_sort), 1):
            draw_one_bar(to_sort[i], "green")
        time.sleep(0.5)
        for i in range(int(len(to_sort)/2)):
            draw_one_bar(to_sort[i], "blue")
        for i in range(int(len(to_sort)/2), len(to_sort), 1):
            draw_one_bar(to_sort[i], "blue")

        result_1 = merge_sort(right[:int(len(right)/2)], right[int(len(right)/2):], right)
        for i, result in enumerate(result_1):
            draw_one_bar(right[i], "white")
            right[i].height = result.height
            draw_one_bar(right[i], "blue")
            time.sleep(0.1)
        result_2 = merge_sort(left[:int(len(left) / 2)], left[int(len(left) / 2):], left)
        for i, result in enumerate(result_2):
            draw_one_bar(left[i], "white")
            left[i].height = result.height
            draw_one_bar(left[i], "blue")
            time.sleep(0.1)

    local = [Bar(element.height, element.index) for element in right + left]
    i = 0
    j = 0
    k = 0

    while i < len(right) and j < len(left):
        if right[i].height < left[j].height:
            local[k].height = right[i].height

            # draw_one_bar(right[i], "black")
            # time.sleep(1)
            i += 1
        else:
            local[k].height = left[j].height
            j += 1
        k += 1
    while i < len(right):
        local[k].height = right[i].height
        i += 1
        k += 1
    while j < len(left):
        local[k].height = left[j].height
        j += 1
        k += 1

    return local


def counting_sort(to_sort):
    count = [0 for _ in range(max_height)]

    for i in range(len(to_sort)):
        draw_count_table(count)
        draw_one_bar(to_sort[i], "green")
        time.sleep(0.1)
        count[to_sort[i].height] += 1
        draw_one_bar(to_sort[i], "blue")

    saved = count.copy()
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    step_sorted = [Bar(0, i) for i, element in enumerate(to_sort)]

    for i in range(len(to_sort)):
        draw_count_table(saved, to_sort[i].height, count)
        draw_one_bar(to_sort[i], "red")
        count[to_sort[i].height] -= 1
        saved[to_sort[i].height] -= 1
        step_sorted[count[to_sort[i].height]].height = to_sort[i].height
        draw_one_bar(step_sorted[count[to_sort[i].height]], "blue", True)
        time.sleep(1)
        draw_one_bar(to_sort[i], "blue")

    for i, bar in enumerate(to_sort):
        bar.height = step_sorted[i].height


def bucket_sort(to_sort):
    buckets = [[] for _ in range(int(max_height/100))] if max_height % 100 == 0 else [[] for _ in range(int(
        max_height/100) + 1)]

    for element in to_sort:
        buckets[int(element.height/100)].append(Bar(element.height, element.index))

    i = j = k = 0
    while i < len(to_sort):
        while j < len(buckets):
            while k < len(buckets[j]):
                draw_one_bar(to_sort[i], "white")
                to_sort[i].height = buckets[j][k].height
                draw_one_bar(to_sort[i], "blue")
                buckets[j][k] = to_sort[i]
                k += 1
                i += 1
            j += 1
            k = 0

    draw_bucket_representation(buckets)

    for i, bucket in enumerate(buckets):
        if i == 0:
            insertion_sort(bucket)
        else:
            insertion_sort(bucket, False)
