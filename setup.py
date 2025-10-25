"""
Setup configuration for CarbonTrack AI Agent
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = [
        line.strip()
        for line in requirements_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="carbontrack-ai-agent",
    version="0.1.0",
    author="Ahmed Ul Kabir",
    author_email="your.email@example.com",
    description="An open-source AI agent for automating LinkedIn promotion of projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedul/carbontrack-ai-agent",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "carbontrack=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="ai agent langchain linkedin automation marketing promotion",
    project_urls={
        "Bug Reports": "https://github.com/ahmedul/carbontrack-ai-agent/issues",
        "Source": "https://github.com/ahmedul/carbontrack-ai-agent",
        "Documentation": "https://github.com/ahmedul/carbontrack-ai-agent#readme",
    },
)
