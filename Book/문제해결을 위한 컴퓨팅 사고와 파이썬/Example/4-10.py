n = int(input("3 에서 6사이의 정수를 입력하세요 : "))
sumAngle = 180 * (n-2)
intAngle = sumAngle/n

print("정%d각형의 내각의 합 = %d 도" % (n, sumAngle))
print("정%d각형의 하나의 내각 = %d 도" % (n, intAngle))
