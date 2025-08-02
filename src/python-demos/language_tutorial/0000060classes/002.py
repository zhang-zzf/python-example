from __future__ import annotations

from gc import freeze
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# 运行时检测类型
class Person(BaseModel):
    name: str
    age: int = Field(lt=196, ge=0)  # [0,196)
    sex: str = Field(frozen=True)  # read-only
    address: Optional[str] = None
    phones: list[str] = Field(default_factory=list)

    @field_validator('phones') # noqa
    @classmethod
    def validate_phones(cls, v: list[str]) -> list[str]:
        for phone in v:
            if len(phone) != 14 or not phone.startswith('+86'):
                raise ValueError('phone number must start with +86')
        return v


def main():
    p = Person(name="zhang.zzf", age=18, sex='male', phones=['+86 12345678901'])
    # p = Person(name=18, age=18, sex='male')
    print(p)
    pass


if __name__ == '__main__':
    main()
