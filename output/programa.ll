; ModuleID = "programa"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"fibonacci"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %".4" = load i32, i32* %"n"
  %".5" = icmp sle i32 %".4", 1
  br i1 %".5", label %"if_true", label %"if_false"
if_true:
  %".7" = load i32, i32* %"n"
  ret i32 %".7"
if_false:
  br label %"if_end"
if_end:
  %".10" = load i32, i32* %"n"
  %".11" = sub i32 %".10", 1
  %".12" = call i32 @"fibonacci"(i32 %".11")
  %".13" = load i32, i32* %"n"
  %".14" = sub i32 %".13", 2
  %".15" = call i32 @"fibonacci"(i32 %".14")
  %".16" = add i32 %".12", %".15"
  ret i32 %".16"
}

define i32 @"main"()
{
entry:
  %"nums" = alloca [5 x i32]
  %".2" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 3, i32* %".2"
  %".4" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 1, i32* %".4"
  %".6" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 4, i32* %".6"
  %".8" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 1, i32* %".8"
  %".10" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 5, i32* %".10"
  %"total" = alloca i32
  store i32 0, i32* %"total"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"r" = alloca i32
  %"suma" = alloca i32
  %"j" = alloca i32
  %"msg" = alloca i8*
  br label %"while_cond"
while_cond:
  %".15" = load i32, i32* %"i"
  %".16" = icmp slt i32 %".15", 5
  br i1 %".16", label %"while_body", label %"while_end"
while_body:
  %".18" = load i32, i32* %"i"
  %".19" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".18"
  %".20" = load i32, i32* %".19"
  %".21" = srem i32 %".20", 2
  store i32 %".21", i32* %"r"
  %".23" = load i32, i32* %"r"
  %".24" = icmp eq i32 %".23", 0
  br i1 %".24", label %"if_true", label %"if_false"
while_end:
  store i32 0, i32* %"suma"
  store i32 1, i32* %"j"
  br label %"for_cond"
if_true:
  %".26" = load i32, i32* %"total"
  %".27" = load i32, i32* %"i"
  %".28" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".27"
  %".29" = load i32, i32* %".28"
  %".30" = add i32 %".26", %".29"
  store i32 %".30", i32* %"total"
  br label %"if_end"
if_false:
  br label %"if_end"
if_end:
  %".34" = load i32, i32* %"i"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %"i"
  %".37" = load i32, i32* %"total"
  %".38" = icmp sgt i32 %".37", 10
  br i1 %".38", label %"if_true.1", label %"if_false.1"
if_true.1:
  br label %"while_end"
if_false.1:
  br label %"if_end.1"
if_end.1:
  br label %"while_cond"
after_break:
  br label %"if_end.1"
for_cond:
  %".47" = load i32, i32* %"j"
  %".48" = icmp sle i32 %".47", 10
  br i1 %".48", label %"for_body", label %"for_end"
for_body:
  %".50" = load i32, i32* %"suma"
  %".51" = load i32, i32* %"j"
  %".52" = add i32 %".50", %".51"
  store i32 %".52", i32* %"suma"
  br label %"for_update"
for_update:
  %".55" = load i32, i32* %"j"
  %".56" = add i32 %".55", 1
  store i32 %".56", i32* %"j"
  br label %"for_cond"
for_end:
  %".59" = getelementptr inbounds [17 x i8], [17 x i8]* @".str1", i32 0, i32 0
  store i8* %".59", i8** %"msg"
  %".61" = load i8*, i8** %"msg"
  %".62" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt2", i32 0, i32 0
  %".63" = call i32 (i8*, ...) @"printf"(i8* %".62", i8* %".61")
  %".64" = call i32 @"fibonacci"(i32 10)
  %".65" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt3", i32 0, i32 0
  %".66" = call i32 (i8*, ...) @"printf"(i8* %".65", i32 %".64")
  %".67" = getelementptr inbounds [12 x i8], [12 x i8]* @".str4", i32 0, i32 0
  %".68" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt5", i32 0, i32 0
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68", i8* %".67")
  %".70" = load i32, i32* %"suma"
  %".71" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt6", i32 0, i32 0
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".71", i32 %".70")
  %".73" = getelementptr inbounds [25 x i8], [25 x i8]* @".str7", i32 0, i32 0
  %".74" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt8", i32 0, i32 0
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".74", i8* %".73")
  %".76" = load i32, i32* %"total"
  %".77" = getelementptr inbounds [4 x i8], [4 x i8]* @".fmt9", i32 0, i32 0
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".77", i32 %".76")
  ret i32 0
}

@".str1" = internal constant [17 x i8] c"Fibonacci(10) = \00"
@".fmt2" = internal constant [4 x i8] c"%s\0a\00"
@".fmt3" = internal constant [4 x i8] c"%d\0a\00"
@".str4" = internal constant [12 x i8] c"Suma 1..10:\00"
@".fmt5" = internal constant [4 x i8] c"%s\0a\00"
@".fmt6" = internal constant [4 x i8] c"%d\0a\00"
@".str7" = internal constant [25 x i8] c"Total pares del arreglo:\00"
@".fmt8" = internal constant [4 x i8] c"%s\0a\00"
@".fmt9" = internal constant [4 x i8] c"%d\0a\00"