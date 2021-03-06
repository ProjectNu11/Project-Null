from sqlalchemy import Column, Integer, DateTime, BIGINT, String

from library.orm import Base


class FunctionCallRecord(Base):
    """
    Function call record

    id: Record id
    time: Calling time
    field: Calling field
    supplicant: Calling supplicant
    function: Called module
    """

    __tablename__ = "function_call_record"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    field = Column(BIGINT, nullable=False)
    supplicant = Column(BIGINT, nullable=False)
    function = Column(String(length=4000), nullable=False)


class BlacklistTable(Base):
    """
    BlacklistTable

    field: Field ID, -1 for global, 0 for direct message, >0 for group
    target: Target ID, 0 for group, >0 for user
    time: Time
    reason: Reason
    supplicant: Supplicant ID
    """

    __tablename__ = "blacklist"

    field = Column(BIGINT, nullable=False, primary_key=True)
    target = Column(BIGINT, nullable=False, primary_key=True)
    time = Column(DateTime, nullable=False)
    reason = Column(String(length=4000), nullable=False)
    supplicant = Column(BIGINT, nullable=False)
