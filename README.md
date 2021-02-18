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





기타. 로컬 컴퓨터에 다음의 코드로 PySpark 설치
 * 하지만 이 방법으로 PySpark 모듈을 설치하는 경우, 모든 PySpark의 기능이 포함되어 있지 않게 된다. 
 
<pre>
<code>
pip install pyspark 
</code>
</pre>


>The Python packaging for Spark is not intended to replace all of the other use cases. This Python packaged version of Spark is suitable for interacting with an >existing cluster (be it Spark standalone, YARN, or Mesos) - but does not contain the tools required to setup your own standalone Spark cluster. You can download >the full version of Spark from the Apache Spark downloads page.

>NOTE: If you are using this with a Spark standalone cluster you must ensure that the version (including minor version) matches or you may experience odd errors



