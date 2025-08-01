#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用用户提供的数据测试冒泡排序
数据: 9, 8, 7, 6, 5, 4, 3, 1
"""

def bubble_sort(arr):
    """
    冒泡排序算法
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"原始数组: {arr}")
    print("开始排序过程:")
    
    for i in range(n):
        swapped = False
        print(f"\n第{i+1}轮排序:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  交换 {arr[j+1]} 和 {arr[j]}: {arr}")
        
        if not swapped:
            print(f"  第{i+1}轮完成，数组已有序")
            break
        else:
            print(f"  第{i+1}轮完成: {arr}")
    
    return arr

def main():
    """主函数"""
    # 用户提供的数据
    user_data = [9, 8, 7, 6, 5, 4, 3, 1]
    
    print("=" * 50)
    print("冒泡排序演示")
    print("=" * 50)
    print(f"输入数据: {user_data}")
    print()
    
    # 执行冒泡排序
    sorted_data = bubble_sort(user_data)
    
    print("\n" + "=" * 50)
    print("排序结果")
    print("=" * 50)
    print(f"排序前: {user_data}")
    print(f"排序后: {sorted_data}")
    
    # 验证结果
    expected = sorted(user_data)
    if sorted_data == expected:
        print("✅ 排序正确!")
    else:
        print("❌ 排序错误!")
    
    print(f"\n数组长度: {len(user_data)}")
    print(f"排序后数组: {sorted_data}")

if __name__ == "__main__":
    main() 