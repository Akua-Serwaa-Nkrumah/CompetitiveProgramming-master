m, n = map(int,input().split())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

ptr1, ptr2 = 0, 0
temp_array = []
while ptr1 < m and ptr2 < n:
    if nums1[ptr1] <= nums2[ptr2]:
        temp_array.append(nums1[ptr1])
        ptr1 += 1
    elif nums2[ptr2] < nums1[ptr1]:
        temp_array.append(nums2[ptr2])
        ptr2 +=1

if ptr1 >= m:
    temp_array.extend(nums2[ptr2:n])

if ptr2 >= n:
    temp_array.extend(nums1[ptr1:m])

print(*temp_array)