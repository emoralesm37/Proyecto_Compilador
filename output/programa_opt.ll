; ModuleID = '/tmp/ir_orig_1tdjccjd.ll'
source_filename = "/tmp/ir_orig_1tdjccjd.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str1 = internal constant [17 x i8] c"Fibonacci(10) = \00"
@.str5 = internal constant [4 x i8] c"%d\0A\00"
@.str6 = internal constant [12 x i8] c"Suma 1..10:\00"
@.str10 = internal constant [4 x i8] c"%d\0A\00"
@.str11 = internal constant [25 x i8] c"Total pares del arreglo:\00"
@.str15 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nosync nounwind memory(none)
define i32 @fibonacci(i32 %.1) local_unnamed_addr #1 {
entry:
  %.54 = icmp slt i32 %.1, 2
  br i1 %.54, label %common.ret, label %if_end

common.ret:                                       ; preds = %if_end, %entry
  %accumulator.tr.lcssa = phi i32 [ 0, %entry ], [ %.16, %if_end ]
  %.1.tr.lcssa = phi i32 [ %.1, %entry ], [ %.14, %if_end ]
  %accumulator.ret.tr = add i32 %.1.tr.lcssa, %accumulator.tr.lcssa
  ret i32 %accumulator.ret.tr

if_end:                                           ; preds = %entry, %if_end
  %.1.tr6 = phi i32 [ %.14, %if_end ], [ %.1, %entry ]
  %accumulator.tr5 = phi i32 [ %.16, %if_end ], [ 0, %entry ]
  %.11 = add nsw i32 %.1.tr6, -1
  %.12 = tail call i32 @fibonacci(i32 %.11)
  %.14 = add nsw i32 %.1.tr6, -2
  %.16 = add i32 %.12, %accumulator.tr5
  %.5 = icmp ult i32 %.1.tr6, 4
  br i1 %.5, label %common.ret, label %if_end
}

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %nums = alloca [5 x i32], align 16
  store <4 x i32> <i32 3, i32 1, i32 4, i32 1>, ptr %nums, align 16
  %.10 = getelementptr inbounds [5 x i32], ptr %nums, i64 0, i64 4
  store i32 5, ptr %.10, align 16
  br label %while_body

while_body:                                       ; preds = %entry, %while_body
  %indvars.iv = phi i64 [ 0, %entry ], [ %indvars.iv.next, %while_body ]
  %total.0 = phi i32 [ 0, %entry ], [ %spec.select, %while_body ]
  %.19 = getelementptr inbounds [5 x i32], ptr %nums, i64 0, i64 %indvars.iv
  %.20 = load i32, ptr %.19, align 4
  %0 = and i32 %.20, 1
  %.24 = icmp eq i32 %0, 0
  %.30 = select i1 %.24, i32 %.20, i32 0
  %spec.select = add i32 %.30, %total.0
  %indvars.iv.next = add nuw nsw i64 %indvars.iv, 1
  %.38 = icmp slt i32 %spec.select, 11
  %.16 = icmp ult i64 %indvars.iv, 4
  %or.cond = and i1 %.16, %.38
  br i1 %or.cond, label %while_body, label %for_cond.preheader

for_cond.preheader:                               ; preds = %while_body
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str1)
  %.64 = tail call i32 @fibonacci(i32 10)
  %.66 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str5, i32 %.64)
  %puts10 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str6)
  %.72 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str10, i32 55)
  %puts11 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str11)
  %.78 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str15, i32 %spec.select)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
attributes #1 = { nofree nosync nounwind memory(none) }
