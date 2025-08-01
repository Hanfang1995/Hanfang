#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版冒泡排序算法实现
包含可视化、性能测试和多种优化版本
"""

import time
import random
from typing import List, Tuple

def bubble_sort_basic(arr: List[int]) -> List[int]:
    """
    基础冒泡排序算法
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def bubble_sort_optimized(arr: List[int]) -> List[int]:
    """
    优化版冒泡排序算法
    添加了提前退出机制，如果一轮中没有交换，说明已经排序完成
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr

def bubble_sort_visual(arr: List[int]) -> Tuple[List[int], int]:
    """
    可视化版冒泡排序，返回排序后的数组和交换次数
    """
    arr = arr.copy()
    n = len(arr)
    swap_count = 0
    
    print("开始排序过程:")
    print(f"初始数组: {arr}")
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swap_count += 1
                print(f"第{swap_count}次交换: {arr}")
        
        if not swapped:
            print(f"第{i+1}轮完成，数组已有序")
            break
        else:
            print(f"第{i+1}轮完成: {arr}")
    
    return arr, swap_count

def performance_test():
    """
    性能测试函数
    """
    print("=" * 50)
    print("性能测试")
    print("=" * 50)
    
    # 测试不同大小的数组
    test_sizes = [100, 500, 1000]
    
    for size in test_sizes:
        # 生成随机数组
        test_array = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\n测试数组大小: {size}")
        
        # 测试基础版本
        start_time = time.time()
        result1 = bubble_sort_basic(test_array.copy())
        basic_time = time.time() - start_time
        
        # 测试优化版本
        start_time = time.time()
        result2 = bubble_sort_optimized(test_array.copy())
        optimized_time = time.time() - start_time
        
        print(f"基础版本耗时: {basic_time:.4f}秒")
        print(f"优化版本耗时: {optimized_time:.4f}秒")
        print(f"性能提升: {((basic_time - optimized_time) / basic_time * 100):.2f}%")
        
        # 验证结果正确性
        if result1 == result2 == sorted(test_array):
            print("✅ 排序结果正确")
        else:
            print("❌ 排序结果错误")

def main():
    """主函数"""
    print("=" * 50)
    print("冒泡排序算法演示")
    print("=" * 50)
    
    # 测试数据
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [1],  # 单个元素
        []     # 空数组
    ]
    
    for i, test_data in enumerate(test_cases, 1):
        print(f"\n--- 测试用例 {i} ---")
        print(f"输入: {test_data}")
        
        if not test_data:
            print("空数组，跳过排序")
            continue
        
        # 基础版本
        result_basic = bubble_sort_basic(test_data)
        print(f"基础版本结果: {result_basic}")
        
        # 优化版本
        result_optimized = bubble_sort_optimized(test_data)
        print(f"优化版本结果: {result_optimized}")
        
        # 验证结果
        expected = sorted(test_data)
        if result_basic == result_optimized == expected:
            print("✅ 排序正确")
        else:
            print("❌ 排序错误")
    
    # 可视化演示
    print(f"\n--- 可视化演示 ---")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    result, swaps = bubble_sort_visual(demo_array)
    print(f"总共交换次数: {swaps}")
    
    # 性能测试
    performance_test()

if __name__ == "__main__":
    main() 