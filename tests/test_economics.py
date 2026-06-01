"""Tests for economics module."""
import pytest
from mining import economics as econ


class TestNPV:
    def test_npv_simple(self):
        """Test basic NPV calculation."""
        # $100 annual cash flow for 3 years, 10% discount
        cf = [100, 100, 100]
        result = econ.npv(0.10, cf, 0)
        # PV = 100/1.1 + 100/1.1^2 + 100/1.1^3 = 90.91 + 82.64 + 75.13 = 248.68
        assert 240 < result < 260

    def test_npv_with_initial_investment(self):
        """Test NPV with initial investment."""
        cf = [50, 50, 50]
        result = econ.npv(0.10, cf, 100)  # $100 upfront
        # PV = 45.45 + 41.32 + 37.57 = 124.34, NPV = 124.34 - 100 = 24.34 (positive)
        assert result > 0  # This project is economic

    def test_npv_negative_discount_rate_raises(self):
        """Test that negative discount rate raises ValueError."""
        with pytest.raises(ValueError):
            econ.npv(-0.05, [100, 100], 0)


class TestPayback:
    def test_simple_payback(self):
        """Test simple payback period."""
        # $100 investment, $25/year return
        result = econ.payback_period(100, 25)
        assert result == 4.0

    def test_payback_never(self):
        """Test payback when cash flow is zero."""
        result = econ.payback_period(100, 0)
        assert result == float('inf')

    def test_discounted_payback(self):
        """Test discounted payback takes longer."""
        simple = econ.payback_period(100, 25)
        discounted = econ.payback_period(100, 25, 0.10)
        assert discounted > simple


class TestCostCalculations:
    def test_mining_cost_per_tonne(self):
        """Test cost per tonne calculation."""
        result = econ.mining_cost_per_tonne(100000, 50000, 25000, 10000)
        # (100k + 50k + 25k) / 10k = $17.50/t
        assert result == 17.5

    def test_mining_cost_zero_tonnes_raises(self):
        """Test zero tonnes raises error."""
        with pytest.raises(ValueError):
            econ.mining_cost_per_tonne(100, 50, 25, 0)


class TestRevenue:
    def test_revenue_per_year(self):
        """Test annual revenue calculation."""
        # 1 Mt @ 3 g/t, 90% recovery, $1800/oz
        result = econ.revenue_per_year(1_000_000, 3.0, 90, 1800)
        # 1M t * 3 g/t * 0.9 / 31.1035 g/oz * $1800/oz
        # Expected around $156M
        assert 150_000_000 < result < 160_000_000

    def test_revenue_invalid_recovery_raises(self):
        """Test invalid recovery raises error."""
        with pytest.raises(ValueError):
            econ.revenue_per_year(1000, 3, 110, 1800)


class TestCutoffGrade:
    def test_cutoff_grade_basic(self):
        """Test cutoff grade calculation."""
        # $85/t OPEX, $1950/oz gold, 92.5% recovery
        result = econ.cutoff_grade(85, 1950, 92.5)
        # Should be around 1.5-1.6 g/t
        assert 1.0 < result < 2.0

    def test_cutoff_grade_invalid_recovery_raises(self):
        """Test zero recovery raises error."""
        with pytest.raises(ValueError):
            econ.cutoff_grade(85, 1950, 0)

    def test_cutoff_grade_negative_net_price_raises(self):
        """Test when selling costs exceed price."""
        with pytest.raises(ValueError):
            econ.cutoff_grade(85, 100, 90, selling_costs_per_oz=150)


class TestSensitivity:
    def test_sensitivity_npv(self):
        """Test sensitivity analysis."""
        changes = {
            "gold_price": (1800, 2000, 15_000_000),
            "grade": (3.0, 2.5, 5_000_000)
        }
        result = econ.sensitivity_npv(10_000_000, changes)
        assert "gold_price" in result
        assert "grade" in result

    def test_tornado_ranking(self):
        """Test tornado chart ranking."""
        sensitivities = {
            "param1": {"npv_change": 10},
            "param2": {"npv_change": -20},
            "param3": {"npv_change": 5}
        }
        ranked = econ.tornado_ranking(sensitivities)
        # param2 has largest absolute change
        assert ranked[0][0] == "param2"


class TestMonteCarloRemoved:
    """The stub monte_carlo_npv_simulation was removed. Verify it is gone."""

    def test_monte_carlo_not_exposed(self):
        assert not hasattr(econ, "monte_carlo_npv_simulation"), (
            "monte_carlo_npv_simulation should be deleted (was a stub returning zeros)"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
