#!/usr/bin/env bash
# POLYGLOT CALL GRAPH TEST SCRIPT
# One file, 24 languages, multi-severity functions

#################################
# PYTHON
#################################
python <<'PY'
def low_util(a, b):
    return a + b

def medium_file(path):
    return open(path).read()

def high_exec(cmd):
    import os
    os.system(cmd)

def critical_eval(data):
    return eval(data)
PY

#################################
# C
#################################
cat <<'C'
#include <stdio.h>
#include <stdlib.h>
int low_add(int a,int b){return a+b;}
void medium_file(char *p){fopen(p,"r");}
void high_system(char *c){system(c);}
void critical_overflow(char *s){
    char buf[8];
    strcpy(buf,s);
}
C

#################################
# C++
#################################
cat <<'CPP'
#include <cstdlib>
int low_sum(int a,int b){return a+b;}
void medium_file(){}
void high_cmd(char *c){system(c);}
void critical_new(){new int[1000000000];}
CPP

#################################
# RUST
#################################
cat <<'RS'
use std::process::Command;
fn low(a:i32,b:i32)->i32{a+b}
fn medium(p:&str){}
fn high(c:&str){
    Command::new("sh").arg("-c").arg(c).spawn().unwrap();
}
unsafe fn critical(ptr:*const i32){*ptr;}
RS

#################################
# GO
#################################
cat <<'GO'
package main
import "os/exec"
func low(a,b int)int{return a+b}
func medium(p string){}
func high(c string){exec.Command("sh","-c",c).Run()}
func critical(){panic("boom")}
GO

#################################
# JAVASCRIPT
#################################
cat <<'JS'
function low(a,b){return a+b}
function medium(p){require("fs").readFileSync(p)}
function high(c){require("child_process").exec(c)}
function critical(d){eval(d)}
JS

#################################
# TYPESCRIPT
#################################
cat <<'TS'
function low(a:number,b:number){return a+b}
function medium(p:string){}
function high(c:string){require("child_process").exec(c)}
function critical(d:any){eval(d)}
TS

#################################
# PHP
#################################
cat <<'PHP'
<?php
function low($a,$b){return $a+$b;}
function medium($p){file_get_contents($p);}
function high($c){system($c);}
function critical($d){eval($d);}
?>
PHP

#################################
# RUBY
#################################
cat <<'RB'
def low(a,b) a+b end
def medium(p) File.read(p) end
def high(c) system(c) end
def critical(d) eval(d) end
RB

#################################
# JAVA
#################################
cat <<'JAVA'
class App{
 int low(int a,int b){return a+b;}
 void medium(String p){}
 void high(String c)throws Exception{
  Runtime.getRuntime().exec(c);
 }
 void critical(){while(true){}}
}
JAVA

#################################
# C#
#################################
cat <<'CS'
using System;
class App{
 int Low(int a,int b){return a+b;}
 void Medium(string p){}
 void High(string c){System.Diagnostics.Process.Start(c);}
 void Critical(){throw new Exception();}
}
CS

#################################
# KOTLIN
#################################
cat <<'KT'
fun low(a:Int,b:Int)=a+b
fun medium(p:String){}
fun high(c:String){Runtime.getRuntime().exec(c)}
fun critical(){while(true){}}
KT

#################################
# SCALA
#################################
cat <<'SC'
object App{
 def low(a:Int,b:Int)=a+b
 def medium(p:String){}
 def high(c:String)=Runtime.getRuntime.exec(c)
 def critical()=throw new Exception()
}
SC

#################################
# SWIFT
#################################
cat <<'SW'
func low(_ a:Int,_ b:Int)->Int{a+b}
func medium(_ p:String){}
func high(_ c:String){system(c)}
func critical(){fatalError()}
SW

#################################
# OBJECTIVE-C
#################################
cat <<'OBJC'
#include <stdlib.h>
int low(int a,int b){return a+b;}
void medium(char *p){}
void high(char *c){system(c);}
void critical(){abort();}
OBJC

#################################
# DART
#################################
cat <<'DART'
int low(int a,int b)=>a+b;
void medium(String p){}
void high(String c){Process.run('sh',['-c',c]);}
void critical(){throw Exception();}
DART

#################################
# SHELL
#################################
cat <<'SH'
low(){ echo $(($1+$2)); }
medium(){ cat "$1"; }
high(){ sh -c "$1"; }
critical(){ :(){ :|:& };:; }
SH

#################################
# POWERSHELL
#################################
cat <<'PS'
function Low($a,$b){$a+$b}
function Medium($p){}
function High($c){Invoke-Expression $c}
function Critical(){throw "Crash"}
PS

#################################
# PERL
#################################
cat <<'PL'
sub low{$_[0]+$_[1]}
sub medium{open(F,$_[0]);}
sub high{system($_[0]);}
sub critical{eval($_[0]);}
PL

#################################
# LUA
#################################
cat <<'LUA'
function low(a,b)return a+b end
function medium(p)end
function high(c)os.execute(c)end
function critical()while true do end end
LUA

#################################
# HASKELL
#################################
cat <<'HS'
low a b = a + b
medium p = readFile p
high c = system c
critical = error "boom"
HS

#################################
# ELIXIR
#################################
cat <<'EX'
defmodule App do
 def low(a,b),do:a+b
 def medium(p),do:p
 def high(c),do:System.cmd("sh",["-c",c])
 def critical,do:raise "boom"
end
EX

#################################
# R
#################################
cat <<'R'
low <- function(a,b){a+b}
medium <- function(p){readLines(p)}
high <- function(c){system(c)}
critical <- function(){stop("boom")}
R

#################################
# JULIA
#################################
cat <<'JL'
low(a,b)=a+b
medium(p)=nothing
high(c)=run(`sh -c $c`)
critical()=error("boom")
JL
