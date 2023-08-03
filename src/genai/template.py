from typing import List, Dict
from pydantic import BaseModel, Field
from genai.schemas import Descriptions as tx


class TemplateData(BaseModel):
    """ A class to handle the template data structure of the WatsonX AI calls """
    instruction: str = Field(description=tx.TEMPLATE_INSTRUCTION)
    input_prefix: str = Field(description=tx.TEMPLATE_INPUT_PREFIX)
    output_prefix: str = Field(description=tx.TEMPLATE_OUTPUT_PREFIX)
    examples: List[Dict] = Field(description=tx.TEMPLATE_EXAMPLES)


class Template(BaseModel):
    """ A class to handle the template structure of the WatsonX AI calls """
    id: str = Field(description=tx.TEMPLATE_DATA)
    data: TemplateData = Field(description=tx.TEMPLATE_DATA)

    def toJSON(self):
        return {
            "id": self.id,
            "data": {
                "instruction": self.data.instruction,
                "input_prefix": self.data.input_prefix,
                "output_prefix": self.data.output_prefix,
                "examples": self.data.examples,
            }
        }
