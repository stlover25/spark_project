spark_project
=============

* 스파크의 다양한 기능들을 살펴보는 프로젝트입니다.
* 우선적으로 파이썬용 스파크 기능을 탐색합니다.



1. 스파크의 공식 홈페이지에서 패키지 유형을 'pre-built for hadoop 2.7'로 선택하고 다운로드 한다.
 * https://spark.apache.org/downloads.html


2. 다운로드한 파일을 /User/cara/local/spark 에 넣는다.

3. 환경 변수에 /Users/soyoon-yoon/local_spark/spark/bin 를 추가한다. (ex. bash_profile)

<pre>
<code>
export PATH=${PATH}:/Users/your_path/local/spark/bin
</code>
</pre>

4. 다음의 명령어를 통해서 Spark가 잘 설치되어 있는지 확인한다. 
<pre>
<code>
spark-shell
</code>
</pre>

다음의 화면이 뜬다면 설치가 성공!

<pre>
<code>
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.7
      /_/
         
Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_251)
Type in expressions to have them evaluated.
Type :help for more information.

scala>
</code>
</pre>

5. 파이썬 아나콘다에서 pyspark 모듈을 사용하고자 하는 경우
* 콘솔창에서 pip install findspark로 findspark를 설치한 후, 아나콘다 창에서 spark가 설치된 경로 지정한다.

<pre>
<code>
import findspark
findspark.init('/path/to/spark_home')
import pyspark
</code>
</pre>


6. 기타) 로컬 컴퓨터에 다음의 코드로 PySpark 설치하는 경우
 * 하지만 이 방법으로 PySpark 모듈을 설치하는 경우, 모든 PySpark의 기능이 포함되어 있지 않게 된다. 
 
<pre>
<code>
pip install pyspark 
</code>
</pre>


>The Python packaging for Spark is not intended to replace all of the other use cases. This Python packaged version of Spark is suitable for interacting with an >existing cluster (be it Spark standalone, YARN, or Mesos) - but does not contain the tools required to setup your own standalone Spark cluster. You can download >the full version of Spark from the Apache Spark downloads page.

>NOTE: If you are using this with a Spark standalone cluster you must ensure that the version (including minor version) matches or you may experience odd errors


Main Error 
=============
1. 
<pre>
<code>
WARN Utils: Your hostname, cara.local resolves to a loopback address: 127.0.0.1; using 172.30.1.11 instead (on interface en0)
</code>
</pre>

* Spark가 설치될 때, spark/conf/spark-env.sh 파일이 설치되어 있지 않다. 
* 따라서, spark/conf/spark-env.sh.template 을 복사하여, .sh로 확장자로 바꿔준 뒤(spark-env.sh 생성) 필요한 코드만 추가하여 사용한다. 
* spark-env.sh 파일을 열고 다음의 코드를 입력한다. 
<pre>
<code>
export SPARK_LOCAL_IP='your ip address'
</code>
</pre>



