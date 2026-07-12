# Python 타입 힌트 정리

파이썬의 타입 힌트는 기본적으로 런타임 강제 장치가 아니라 정적 분석용 힌트다.  
그래서 `Literal`, `NewType`, `TypeAlias`를 써도 파이썬 실행기 자체가 자동으로 예외를 던지지는 않는다.

이 문서는 아래 내용을 한 번에 정리한다.

- 왜 실행은 되는데 IDE에서 에러가 안 보일 수 있는가
- `TypeAlias`, `Literal`, `NewType`의 차이
- 언제 무엇을 쓰면 좋은가
- VS Code에서 정적 타입 오류를 보이게 하는 방법
- 이 저장소의 예제 파일과 연결해서 보는 방법

## 1. 핵심 개념

### 런타임 검사와 정적 타입 검사는 다르다

파이썬은 기본적으로 동적 타입 언어다. 타입 힌트는 문법에 포함되어 있지만, 파이썬 런타임이 이를 자동으로 강제하지는 않는다.

예를 들어:

```python
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    print(f"Setting log level to {level}")

set_log_level("DEBUG")
set_log_level("CRITICAL")
```

위 코드는 실행 자체는 된다.  
이유는 `"CRITICAL"`도 런타임에서는 그냥 `str`이기 때문이다.

즉:

- 파이썬 실행: 통과 가능
- 타입 체커: 오류로 판단해야 정상

공식 문서도 타입 어노테이션은 런타임이 아니라 타입 체커, IDE, 린터 같은 외부 도구가 활용한다고 설명한다.

## 2. `TypeAlias`, `Literal`, `NewType` 차이

### `TypeAlias`: 별명 붙이기

복잡한 타입에 읽기 좋은 이름을 붙이고 싶을 때 쓴다.

```python
from typing import TypeAlias

UserId: TypeAlias = int
ProductId: TypeAlias = int
```

중요한 점은 `UserId`와 `ProductId`가 논리적으로는 달라도, 타입 체커 입장에서는 둘 다 결국 `int`라는 점이다.  
즉 타입을 구분하는 용도가 아니라, 타입 표현을 간단하게 만드는 용도다.

이 저장소 예제:

- `architecture/type-hinting/alias.py`

언제 쓰나:

- 복잡한 컬렉션 타입을 짧게 표현하고 싶을 때
- 도메인 의미를 이름으로 드러내고 싶을 때
- 구분보다는 가독성이 목적일 때

### `Literal`: 가능한 값 자체를 제한

타입이 아니라 "허용 가능한 정확한 값"을 제한하고 싶을 때 쓴다.

```python
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
```

이 타입은 `str`의 하위 집합처럼 동작한다.  
아무 문자열이나 되는 것이 아니라, 지정한 문자열만 허용한다.

이 저장소 예제:

- `architecture/type-hinting/literal.py`

언제 쓰나:

- 로그 레벨
- 정해진 명령 문자열
- API 옵션 값
- 모드 이름처럼 선택지가 고정된 경우

### `NewType`: 같은 기반 타입이지만 논리적으로 다른 타입으로 구분

런타임 비용은 거의 없이, 타입 체커에게는 서로 다른 타입처럼 보이게 만들고 싶을 때 쓴다.

```python
from typing import NewType

UserId = NewType("UserId", int)
ProductId = NewType("ProductId", int)
```

이렇게 만들면:

- `UserId`는 `int` 기반
- `ProductId`도 `int` 기반
- 하지만 타입 체커는 둘을 다른 타입으로 취급

예:

```python
from typing import NewType

UserId = NewType("UserId", int)
ProductId = NewType("ProductId", int)

def process_order(user_id: UserId, product_id: ProductId) -> None:
    print(f"Processing order for User {user_id}, Product {product_id}")

user_id = UserId(1)
product_id = ProductId(1)

process_order(user_id, product_id)   # 정상
process_order(product_id, user_id)   # 타입 체커는 오류로 봐야 함
```

하지만 런타임에서는 둘 다 사실상 `int`처럼 동작하므로 실행은 된다.

이 저장소 예제:

- `architecture/type-hinting/new-type.py`

언제 쓰나:

- `UserId`, `ProductId`, `OrderId`처럼 모두 `int`이지만 절대 섞이면 안 될 때
- `EmailAddress`, `Token`, `CurrencyCode`처럼 문자열 기반이지만 역할이 다를 때
- 단순 별명보다 더 강한 논리적 구분이 필요할 때

## 3. 한 줄 요약

- `TypeAlias`: 타입 별명
- `Literal`: 가능한 값 제한
- `NewType`: 같은 기반 타입을 논리적으로 분리

## 4. 왜 IDE에서 에러가 안 보일 수 있나

보통 이유는 둘 중 하나다.

### 1. 타입 체커가 꺼져 있다

타입 힌트만 적는다고 IDE가 자동으로 엄격한 타입 검사를 다 해주진 않는다.  
에디터가 타입 분석기를 켜고 있어야 한다.

### 2. 타입 검사 강도가 낮다

특히 VS Code + Pylance 환경에서는 타입 검사 강도를 `off`, `basic`, `strict` 등으로 조정할 수 있다.  
`off`면 타입 관련 빨간 줄이 거의 안 보일 수 있다.

## 5. VS Code에서 정적 타입 오류 보이게 하기

가장 쉬운 조합은 아래다.

1. VS Code 설치
2. `Python` 확장 설치
3. `Pylance` 사용
4. 인터프리터 선택
5. `python.analysis.typeCheckingMode`를 `basic` 이상으로 설정

설정 예시:

```json
{
  "python.analysis.typeCheckingMode": "basic"
}
```

좀 더 엄격하게 보고 싶으면:

```json
{
  "python.analysis.typeCheckingMode": "strict"
}
```

이 프로젝트의 현재 워크스페이스 설정은 이미 아래처럼 되어 있다.

```json
{
  "java.debug.settings.onBuildFailureProceed": true,
  "python.analysis.typeCheckingMode": "strict"
}
```

즉 이 워크스페이스를 VS Code에서 열면, `Pylance`가 정상 동작하는 전제에서 타입 오류가 꽤 적극적으로 표시되는 편이어야 한다.

### 기대되는 진단 예시

`architecture/type-hinting/literal.py`

```python
set_log_level("CRITICAL")
```

타입 체커 기대 결과:

- `Literal["DEBUG", "INFO", "WARNING", "ERROR"]`에 없는 값 전달

`architecture/type-hinting/new-type.py`

```python
process_order(product_id, user_id)
```

타입 체커 기대 결과:

- 첫 번째 인자는 `UserId`여야 하는데 `ProductId`가 들어감
- 두 번째 인자는 `ProductId`여야 하는데 `UserId`가 들어감

## 6. 터미널에서 확인하는 방법

IDE 표시와 별개로, 커맨드 라인에서 타입 체크를 돌릴 수도 있다.

대표적으로 `mypy`를 많이 쓴다.

```bash
python -m pip install mypy
mypy architecture/type-hinting/literal.py
mypy architecture/type-hinting/new-type.py
```

`mypy`는 코드를 실행하지 않고 정적으로 검사한다.  
즉 프로그램은 실행 가능하더라도 타입 설계상 문제를 따로 잡아낼 수 있다.

## 7. 런타임에서도 막고 싶다면

타입 힌트만으로는 런타임 검사가 되지 않으므로, 실제 실행 중에도 잘못된 값을 막고 싶다면 직접 검사 코드를 넣어야 한다.

예:

```python
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError(f"Invalid log level: {level}")
    print(f"Setting log level to {level}")
```

즉:

- 정적 타입 체커: 개발 중 실수 예방
- 런타임 검사: 실제 실행 중 잘못된 입력 방어

둘은 역할이 다르다.

## 8. 무엇을 언제 쓸까

### `TypeAlias`를 쓰면 좋은 경우

- 타입 표현이 너무 길다
- 도메인 의미를 이름으로 드러내고 싶다
- 실제로는 같은 타입으로 취급되어도 괜찮다

예:

```python
type UserRecord = dict[str, str]
```

### `Literal`을 쓰면 좋은 경우

- 허용 가능한 값 후보가 몇 개로 고정되어 있다
- 문자열 오타를 IDE 단계에서 잡고 싶다
- enum까지는 필요 없고 가벼운 값 제한이 필요하다

예:

```python
Mode = Literal["read", "write", "append"]
```

### `NewType`을 쓰면 좋은 경우

- 기반 타입은 같지만 섞이면 위험하다
- 숫자 ID나 문자열 토큰을 논리적으로 분리하고 싶다
- 타입 체커가 도메인 혼동을 잡아주길 원한다

예:

```python
CustomerId = NewType("CustomerId", int)
OrderId = NewType("OrderId", int)
```

## 9. 자주 하는 오해

### 오해 1. 타입 힌트를 달면 파이썬이 자동으로 검사한다

아니다. 기본 파이썬 런타임은 자동 강제를 하지 않는다.

### 오해 2. `NewType`은 진짜 새 클래스를 만든다

아니다. 타입 체커 관점에서 구분하기 위한 장치에 가깝다.  
런타임에서는 매우 가볍게 동작한다.

### 오해 3. `TypeAlias`면 다른 타입처럼 분리된다

아니다. 별명일 뿐이다.  
구분이 목적이면 `NewType`이 더 적합하다.

### 오해 4. `Literal`은 실행 중에도 값이 자동 차단된다

아니다. 타입 체커가 개발 단계에서 잡는 것이다.  
실행 중 차단은 별도 검사 코드가 필요하다.

## 10. 추천 학습 순서

1. 기본 함수 타입 힌트
2. `list[str]`, `dict[str, int]` 같은 컬렉션 타입
3. `TypeAlias`
4. `Literal`
5. `NewType`
6. 필요해지면 `Protocol`, `TypedDict`, `Generic`

## 참고 자료

- Python `typing` 공식 문서: https://docs.python.org/3/library/typing.html
- VS Code Python 설정 문서: https://code.visualstudio.com/docs/python/settings-reference
- VS Code Python linting/type checking 문서: https://code.visualstudio.com/docs/python/linting
- mypy 시작 문서: https://mypy.readthedocs.io/en/stable/getting_started.html
