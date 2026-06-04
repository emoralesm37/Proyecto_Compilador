; ModuleID = "programa_v4"
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
  %"nums" = alloca [6 x i32]
  %".2" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 0
  store i32 3, i32* %".2"
  %".4" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 1
  store i32 1, i32* %".4"
  %".6" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 2
  store i32 4, i32* %".6"
  %".8" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 3
  store i32 1, i32* %".8"
  %".10" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 4
  store i32 5, i32* %".10"
  %".12" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 5
  store i32 8, i32* %".12"
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
  %".17" = load i32, i32* %"i"
  %".18" = icmp slt i32 %".17", 6
  br i1 %".18", label %"while_body", label %"while_end"
while_body:
  %".20" = load i32, i32* %"i"
  %".21" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 %".20"
  %".22" = load i32, i32* %".21"
  %".23" = srem i32 %".22", 2
  store i32 %".23", i32* %"r"
  %".25" = load i32, i32* %"r"
  %".26" = icmp eq i32 %".25", 0
  br i1 %".26", label %"if_true", label %"if_false"
while_end:
  store i32 0, i32* %"suma"
  store i32 1, i32* %"j"
  br label %"for_cond"
if_true:
  %".28" = load i32, i32* %"total"
  %".29" = load i32, i32* %"i"
  %".30" = getelementptr inbounds [6 x i32], [6 x i32]* %"nums", i32 0, i32 %".29"
  %".31" = load i32, i32* %".30"
  %".32" = add i32 %".28", %".31"
  store i32 %".32", i32* %"total"
  br label %"if_end"
if_false:
  br label %"if_end"
if_end:
  %".36" = load i32, i32* %"i"
  %".37" = add i32 %".36", 1
  store i32 %".37", i32* %"i"
  %".39" = load i32, i32* %"total"
  %".40" = icmp sgt i32 %".39", 10
  br i1 %".40", label %"if_true.1", label %"if_false.1"
if_true.1:
  br label %"while_end"
if_false.1:
  br label %"if_end.1"
if_end.1:
  br label %"while_cond"
after_break:
  br label %"if_end.1"
for_cond:
  %".49" = load i32, i32* %"j"
  %".50" = icmp sle i32 %".49", 11
  br i1 %".50", label %"for_body", label %"for_end"
for_body:
  %".52" = load i32, i32* %"suma"
  %".53" = load i32, i32* %"j"
  %".54" = add i32 %".52", %".53"
  store i32 %".54", i32* %"suma"
  br label %"for_update"
for_update:
  %".57" = load i32, i32* %"j"
  %".58" = add i32 %".57", 1
  store i32 %".58", i32* %"j"
  br label %"for_cond"
for_end:
  %".61" = getelementptr inbounds [17 x i8], [17 x i8]* @".str1", i32 0, i32 0
  store i8* %".61", i8** %"msg"
  %".63" = load i8*, i8** %"msg"
  %".64" = getelementptr inbounds [4 x i8], [4 x i8]* @".str3", i32 0, i32 0
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", i8* %".63")
  %".66" = call i32 @"fibonacci"(i32 10)
  %".67" = getelementptr inbounds [4 x i8], [4 x i8]* @".str5", i32 0, i32 0
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", i32 %".66")
  %".69" = getelementptr inbounds [12 x i8], [12 x i8]* @".str6", i32 0, i32 0
  %".70" = getelementptr inbounds [4 x i8], [4 x i8]* @".str8", i32 0, i32 0
  %".71" = call i32 (i8*, ...) @"printf"(i8* %".70", i8* %".69")
  %".72" = load i32, i32* %"suma"
  %".73" = getelementptr inbounds [4 x i8], [4 x i8]* @".str10", i32 0, i32 0
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73", i32 %".72")
  %".75" = getelementptr inbounds [25 x i8], [25 x i8]* @".str11", i32 0, i32 0
  %".76" = getelementptr inbounds [4 x i8], [4 x i8]* @".str13", i32 0, i32 0
  %".77" = call i32 (i8*, ...) @"printf"(i8* %".76", i8* %".75")
  %".78" = load i32, i32* %"total"
  %".79" = getelementptr inbounds [4 x i8], [4 x i8]* @".str15", i32 0, i32 0
  %".80" = call i32 (i8*, ...) @"printf"(i8* %".79", i32 %".78")
  ret i32 0
}

@".str1" = internal constant [17 x i8] c"Fibonacci(10) = \00"
@".str3" = internal constant [4 x i8] c"%s\0a\00"
@".str5" = internal constant [4 x i8] c"%d\0a\00"
@".str6" = internal constant [12 x i8] c"Suma 1..10:\00"
@".str8" = internal constant [4 x i8] c"%s\0a\00"
@".str10" = internal constant [4 x i8] c"%d\0a\00"
@".str11" = internal constant [25 x i8] c"Total pares del arreglo:\00"
@".str13" = internal constant [4 x i8] c"%s\0a\00"
@".str15" = internal constant [4 x i8] c"%d\0a\00"