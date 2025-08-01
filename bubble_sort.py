#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序算法实现
"""

def bubble_sort(arr):
    """
    标准冒泡排序算法
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def optimized_bubble_sort(arr):
    """
    优化版冒泡排序算法
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    """主函数"""
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_data)
    
    # 标准冒泡排序
    sorted_data = bubble_sort(test_data.copy())
    print("标准冒泡排序结果:", sorted_data)
    
    # 优化版冒泡排序
    optimized_data = optimized_bubble_sort(test_data.copy())
    print("优化版冒泡排序结果:", optimized_data)
    #ceshi1tuisong

if __name__ == "__main__":
    main() 