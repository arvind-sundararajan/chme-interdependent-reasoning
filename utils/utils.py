```json
{
    "utils/utils.py": {
        "content": "
import logging
from typing import List, Dict
from langfuse import StateGraph
from bardeen import MemoryManager

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the drift index using a stochastic regime switch model
        drift_index = stochastic_regime_switch(data)
        logger.info('Non-stationary drift index calculated successfully')
        return drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(data: List[float]) -> float:
    """
    Calculate the stochastic regime switch for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The stochastic regime switch.
    """
    try:
        # Create a StateGraph using LangGraph
        graph = StateGraph()
        # Add nodes and edges to the graph
        graph.add_node('node1')
        graph.add_edge('node1', 'node2')
        # Calculate the stochastic regime switch using the graph
        regime_switch = graph.calculate_regime_switch(data)
        logger.info('Stochastic regime switch calculated successfully')
        return regime_switch
    except Exception as e:
        logger.error(f'Error calculating stochastic regime switch: {e}')
        raise

def memory_management(data: Dict[str, float]) -> None:
    """
    Manage memory for a given dataset using Letta.

    Args:
    - data (Dict[str, float]): The input dataset.
    """
    try:
        # Create a MemoryManager using Bardeen
        manager = MemoryManager()
        # Manage memory for the dataset
        manager.manage_memory(data)
        logger.info('Memory managed successfully')
    except Exception as e:
        logger.error(f'Error managing memory: {e}')
        raise

def rocket_science_simulation() -> None:
    """
    Simulate the 'Rocket Science' problem.
    """
    try:
        # Create a dataset for the simulation
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        # Calculate the non-stationary drift index
        drift_index = non_stationary_drift_index(data)
        # Manage memory for the dataset
        memory_management({'key': drift_index})
        logger.info('Rocket science simulation completed successfully')
    except Exception as e:
        logger.error(f'Error running rocket science simulation: {e}')
        raise

if __name__ == '__main__':
    rocket_science_simulation()
",
        "commit_message": "feat: implement specialized utils logic"
    }
}
```