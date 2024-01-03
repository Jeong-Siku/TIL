1. Hadoop 구성
   - NameNode(Standby) - Journal - Name Node(Active) - S-Name Node
   - Data Node(Worker) - Data Node(Worker) - Data Node(Worker) .....

하둡 데이터 노드와 스파크 워커는 항상 같은 곳에 위치시킬 것

- 네트워크 통신이 최대한 덜 반복되도록

Spark 기초 개념에서 참고할 것

---

# 카프카

비동기

큐잉

- Queue에 메세지 담고 처리
- Queue : FIFO 방식 자료구조
- Message : 발생되는 중인 데이터, 앞으로 수집할 데이터  
  <-> 배치 : 이미 발생되어 수집된 데이터

Message Queue

### 카프카 대표적인 구성요소

- Producer : 메세지를 생산하는 주체이며 메시지를 Topic로 보내는 애플리케이션
- Consumer : 토픽 내에 들어있는 메시지를 가져와서 소비
- Topic : 메시지가 저장되는 장소를 `논리적으로 표현하는 개념`. In-Memory

### 카프카 내부 구성요소와 아키텍처

![](20230615155033.png)

- Broker : 카프카 서버. Bootstrap Server. Producer와 Consumer가 접속하여 topic을 가져온다. 이중화
- 파티션 : topic이 실제 디스크에 물리적으로 저장되는 기준. 시간 순서를 나타내기 위해 offset이라는 순번을 가진다.

컨슈머 그룹

클러스터 구성

- 여러 대의 서버가 하나의 토픽을 서빙한다.
- 고가용성 : 에러가 나도 계속 진행할 수 있다.

Zookeeper

KIP500

- 쥬키퍼를 카프카랑 분리하려는 프로젝트
- 오픈소스 , Confluent

Avro : 타입이 있는 JSON 형식

토픽이 중요하다. 카프카 파티션은 여러 브로커에 걸쳐서 생성된다.

Round Robin

- 원형으로 돌아가면서 분배. 한바퀴돌면 다시 처음부터

파티션 리더

- 복제된 파티션은 프로듀서와 컨슈머에게 정보를 보내지 않는다. 백업용

컨슈머 그룹

- 각 컨슈머 그룹은 각자 다른 기능을 수행 가능

프로듀서나 컨슈머가 여러개여도 파티션이 한개면 하나의 컨슈머에서만 정보가 출력된다.
