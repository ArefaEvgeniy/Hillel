def func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print("------------------")


func(b=77, r=67, d="Hello", a=100)
func(999, r=67, d="Hello", b=77)
func(999, 56, 77, 67, r=67, d="Hello", b=77)
func(999, 56, 77, 67)
func(r=67, d="Hello", b=77)
func()
