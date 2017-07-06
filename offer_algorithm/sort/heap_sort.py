# !usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


class MaxHead():
    """
    最大堆
    """
    def sift_down(self, arr, start, end):
        root = start
        while True:
            # 从root开始对最大堆调整
            child = 2 * root + 1
            if child > end:
                break

            # 找出两个child中交大的一个
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1

            if arr[root] < arr[child]:
                # 最大堆小于较大的child, 交换顺序
                arr[root], arr[child] = arr[child], arr[root]

                # 正在调整的节点设置为root
                root = child
            else:
                # 无需调整的时候, 退出
                break

    def heap_sort(self, arr):
        # 从最后一个有子节点的孩子还是调整最大堆
        first = len(arr) // 2 - 1
        for start in range(first, -1, -1):
            self.sift_down(arr, start, len(arr) - 1)

        # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
        for end in range(len(arr)-1, -1, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self.sift_down(arr, 0, end - 1)

    def min_n(self, arr, n):
        """
        计算得到arr中的最小的n个数
        :param arr:
        :param n:
        :return:
        """
        if n > len(arr):
            return

        top_n = []
        for i in range(n):
            top_n.append(arr[i])

        # 将当前top_n中的数建成最大堆
        first = len(top_n) // 2 - 1
        for start in range(first, -1, -1):
            self.sift_down(top_n, start, len(top_n) - 1)

        # arr中的n到最后的数逐个与大顶堆比较，比堆顶小时弹出堆顶重新替换为最大堆
        for i in range(n, len(arr)):
            if arr[i] < top_n[0]:
                top_n[0] = arr[i]
                self.sift_down(top_n, 0, len(top_n)-1)
        print top_n


class MinHead():
    """
    最小堆
    """
    def sift_down(self, arr, start, end):
        root = start
        while True:
            # 从root开始对最小堆调整
            child = 2 * root + 1
            if child > end:
                break

            # 找出两个child中交小的一个
            if child + 1 <= end and arr[child] > arr[child + 1]:
                child += 1

            if arr[root] > arr[child]:
                # 最小堆大于较大的child, 交换顺序
                arr[root], arr[child] = arr[child], arr[root]
                # 正在调整的节点设置为root
                root = child
            else:
                # 无需调整的时候, 退出
                break

    def heap_sort(self, arr):
        # 从最后一个有子节点的孩子还是调整最大堆
        first = len(arr) // 2 - 1
        for start in range(first, -1, -1):
            self.sift_down(arr, start, len(arr) - 1)

        # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
        for end in range(len(arr) -1, -1, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self.sift_down(arr, 0, end - 1)

    def max_n(self, arr, n):
        """
        计算得到arr中的最大的n个数
        :param arr:
        :param n:
        :return:
        """
        if n > len(arr):
            return

        top_n = []
        for i in range(n):
            top_n.append(arr[i])

        # 将当前top_n中的数建成最小堆
        first = len(top_n) // 2 - 1
        for start in range(first, -1, -1):
            self.sift_down(top_n, start, len(top_n) - 1)

        # arr中的n到最后的数逐个与小顶堆比较，比堆顶大时弹出堆顶重新替换为最小堆
        for i in range(n, len(arr)):
            if arr[i] > top_n[0]:
                top_n[0] = arr[i]
                self.sift_down(top_n, 0, len(top_n)-1)
        print top_n


def main():
    # [7, 95, 73, 65, 60, 77, 28, 62, 43]
    # [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    hs = MinHead()
    hs.max_n(l, 5)
    print l

if __name__ == "__main__":
    main()
