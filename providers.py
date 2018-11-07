from enum import Enum
from mimesis.enums import Gender
from mimesis.exceptions import NonEnumerableError
from mimesis.helpers import get_random_item
from mimesis.providers.date import Datetime as BaseDataProvider
from mimesis.utils import pull
from typing import List
from typing import Optional
import uuid


__all__ = ['DatasetItem', ]


class StatesBr(Enum):

    AC = 'AC'
    AL = 'AL'
    AM = 'AM'
    AP = 'AP'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MG = 'MG'
    MS = 'MS'
    MT = 'MT'
    PA = 'PA'
    PB = 'PB'
    PE = 'PE'
    PI = 'PI'
    PR = 'PR'
    RJ = 'RJ'
    RN = 'RN'
    RO = 'RO'
    RR = 'RR'
    RS = 'RS'
    SC = 'SC'
    SE = 'SE'
    SP = 'SP'
    TO = 'TO'


class SpiderName(Enum):

    ESAJ = 'ESAJ'
    PJE = 'PJE'
    PROJUDI = 'PROJUDI'


class DatasetItem(BaseDataProvider):

    """Class for generating the dataset."""

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize attributes.

        """
        super().__init__(*args, **kwargs)
        self._data_person = pull('person.json', self.locale)
        self._data_text = pull('text.json', self.locale)
        self.limits = {
            'date_distribuition_limits': (1993, 2015),
            'date_scraping_limits': (2016, 2018),
        }

    def new_item(self):
        """
        Generate a new item for the dataset.

        """
        return {
            'id': self.uuid(),
            'npu': self.npu(),
            'estado': self.state(),
            'spider': self.spider(),
            'juiz': self.full_name(),
            'data_distribuicao': self.date_distribuition(),
            'data_captura': self.date_scraping(),
            'andamentos': self.andamentos()
        }

    def uuid(self, version: Optional[int] = None) -> str:
        """Generate random UUID.
        :param version: UUID version.
        :return: UUID
        """
        bits = self.random.getrandbits(128)
        return str(uuid.UUID(int=bits, version=version))

    def npu(self) -> str:
        """Generate random NPU.

        :return: String with a non valid NPU.

        :Example:
            0001726-07.2011.8.17.1220
        """
        return self.identifier('#######-##.####.#.##.####')

    def state(self, estado: Optional[StatesBr] = None) -> str:
        """Get a random name of state.
        :return: Name of the state.
        :Example:
            PE
        """
        return get_random_item(StatesBr, self.random).value

    def spider(self) -> str:
        """Get a random name of a spider.
        :return: Name of the spider.
        :Example:
            esaj-pe
        """
        state = get_random_item(StatesBr, self.random).value
        spider = get_random_item(SpiderName, self.random).value
        return f'{spider}-{state}'.lower()

    def date_distribuition(self) -> str:
        """Get a date between the limits specified on the class.
        :return: A timestamp string for the distribution date.
        :Example:
            1993-03-23T04:49:29Z
        """
        start, end = self.limits.get('date_distribuition_limits')
        return self.timestamp(posix=False, start=start, end=end)

    def date_scraping(self) -> str:
        """Get a date between the limits specified on the class.
        :return: A timestamp string for the scraping date.
        :Example:
            1993-03-23T04:49:29Z
        """
        start, end = self.limits.get('date_scraping_limits')
        return self.timestamp(posix=False, start=start, end=end)

    def andamento(self, minimum_text: int = 60, maximum_text: int = 350,
                  minimum_tags: int = 1, maximum_tags: int = 5):
        qnt_tags = self.random.randint(int(minimum_tags), int(maximum_tags))
        qnt_texto = self.random.randint(int(minimum_text), int(maximum_text))
        start, end = self.limits.get('date_distribuition_limits')
        return {
            'texto': ' '.join(self.words(quantity=qnt_texto)),
            'data': self.timestamp(posix=False, start=start, end=end),
            'etiquetas': self.tags(qnt_tags),
        }

    def andamentos(self, minimum: int = 5, maximum: int = 80):
        qtd_andamentos = self.random.randint(int(minimum), int(maximum))
        return [self.andamento() for _ in range(qtd_andamentos)]

    def tags(self, quantity: int = 5) -> List[str]:
        """Generate lis of the random tags.
        :param quantity: Quantity of tags. Default is 5.
        :return: Tags list.
        :Example:
            [Red, Blue, Yellow, White, Green]
        """
        tags = self._data_text['color']
        return [self.random.choice(tags) for _ in range(quantity)]

    def words(self, quantity: int = 5) -> List[str]:
        """Generate lis of the random words.
        :param quantity: Quantity of words. Default is 5.
        :return: Word list.
        :Example:
            [science, network, god, octopus, love]
        """
        words = self._data_text['words'].get('normal')
        words_list = [self.random.choice(words) for _ in range(quantity)]
        return words_list

    def name(self, gender: Optional[Gender] = None) -> str:
        """Generate a random name.

        :param gender: Gender's enum object.
        :return: Name.

        :Example:
            John.
        """
        key = self._validate_enum(gender, Gender)
        names = self._data_person['names'].get(key)
        return self.random.choice(names)

    def surname(self, gender: Optional[Gender] = None) -> str:
        """Generate a random surname.
        :param gender: Gender's enum object.
        :return: Surname.
        :Example:
            Smith.
        """
        surnames = self._data_person['surnames']

        # Surnames separated by gender.
        if isinstance(surnames, dict):
            key = self._validate_enum(gender, Gender)
            surnames = surnames[key]

        return self.random.choice(surnames)

    def full_name(self, gender: Optional[Gender] = None,
                  reverse: bool = False) -> str:
        """Generate a random full name.

        :param reverse: Return reversed full name.
        :param gender: Gender's enum object.
        :return: Full name.

        :Example:
            Johann Wolfgang.
        """
        if gender is None:
            gender = get_random_item(Gender, rnd=self.random)

        if gender and isinstance(gender, Gender):
            gender = gender
        else:
            raise NonEnumerableError(Gender)

        fmt = '{1} {0}' if reverse else '{0} {1}'
        return fmt.format(
            self.name(gender),
            self.surname(gender),
        )

    def identifier(self, mask: str = '##-##/##') -> str:
        """Generate a random identifier by mask.

        With this method you can generate any identifiers that
        you need. Simply select the mask that you need.

        :param mask:
            The mask. Here ``@`` is a placeholder for characters and ``#`` is
            placeholder for digits.
        :return: An identifier.

        :Example:
            07-97/04
        """
        return self.random.custom_code(mask=mask)
