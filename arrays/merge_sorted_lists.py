"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.
"""
# %%

def insert(num1, jdx, num2, idx):
    num1.insert(jdx, num2[idx])
    num1.pop(-1)


def merge(nums1, m, nums2, n):
    jdx = 0
    for idx in range(n):
        if m > 0:
            while jdx < m + n:
                if (
                    (nums2[idx] <= nums1[jdx])
                    or (nums1[jdx] == 0 and jdx >= m + idx)
                ):
                    break
                jdx += 1

        print(nums1, jdx, nums2, idx)
        insert(nums1, jdx, nums2, idx)
        jdx += 1


# %%


def test_merge():
    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    m, n = 3, 3
    merge(nums1, m, nums2, n)
    expected_out = [1, 2, 2, 3, 5, 6]
    assert nums1 == expected_out


def test_merge_void():
    nums1, nums2 = [1], []
    m, n = 1, 0
    merge(nums1, m, nums2, n)
    expected_out = [1]
    assert nums1 == expected_out


def test_merge_void():
    nums1, nums2 = [0], [1]
    m, n = 0, 1
    merge(nums1, m, nums2, n)
    expected_out = [1]
    assert nums1 == expected_out


def test_zero():
    nums1, nums2 = [-1, 0, 0, 3, 3, 3, 0, 0, 0], [1, 2, 2]
    m, n = 6, 3
    merge(nums1, m, nums2, n)
    expected_out = [-1, 0, 0, 1, 2, 2, 3, 3, 3]
    assert nums1 == expected_out


def multi_zero():
    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    nums2 = [-1, -1, 0, 0, 1, 2]
    m, n = 5, 6
    merge(nums1, m, nums2, n)
    expected_out = [-1, -1,-1, 0, 0, 0, 0, 0, 1, 2, 3]
    assert nums1 == expected_out