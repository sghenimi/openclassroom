class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    if self.a <= 20:
        self.a += 1
        return (self.a -1)
    else:
        raise StopIteration

my_nums = MyNumbers()
iter_num = iter(my_nums)

print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))

for x in my_nums:
    print("element : ", x)