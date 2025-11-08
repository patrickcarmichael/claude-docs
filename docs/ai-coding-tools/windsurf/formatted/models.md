---
title: "Models"
source: "https://docs.windsurf.com/windsurf/models"
---

# Models
Source: https://docs.windsurf.com/windsurf/models



export const ModelsTable = () => {
  const [showAll, setShowAll] = useState(false);
  const windsurfIcon = {
    light: "https://exafunction.github.io/public/icons/docs/Windsurf-black-symbol.png",
    dark: "https://exafunction.github.io/public/icons/docs/Windsurf-white-symbol.png"
  };
  const openaiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/OpenAI-black-monoblossom.png",
    dark: "https://exafunction.github.io/public/icons/docs/OpenAI-white-monoblossom.png"
  };
  const claudeIcon = {
    light: "https://exafunction.github.io/public/icons/docs/claude-logo-clay.png",
    dark: "https://exafunction.github.io/public/icons/docs/claude-logo-clay.png"
  };
  const deepseekIcon = {
    light: "https://exafunction.github.io/public/icons/docs/deepseek-logo.png",
    dark: "https://exafunction.github.io/public/icons/docs/deepseek-logo.png"
  };
  const geminiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/gemini-models-icon.png",
    dark: "https://exafunction.github.io/public/icons/docs/gemini-models-icon.png"
  };
  const grokIcon = {
    light: "https://exafunction.github.io/public/icons/docs/Grok_Logomark_Dark.png",
    dark: "https://exafunction.github.io/public/icons/docs/Grok_Logomark_Light.png"
  };
  const qwenIcon = {
    light: "https://exafunction.github.io/public/icons/docs/qwen-logo.png",
    dark: "https://exafunction.github.io/public/icons/docs/qwen-logo.png"
  };
  const kimiIcon = {
    light: "https://exafunction.github.io/public/icons/docs/kimi-k2-icon.png",
    dark: "https://exafunction.github.io/public/icons/docs/kimi-k2-icon.png"
  };
  const byokOnly = <a href="/windsurf/models#bring-your-own-key-byok" className="text-gray-700 dark:text-white font-normal">BYOK</a>;
  const apiPricingOnly = <a href="/windsurf/models#api-pricing" className="text-gray-700 dark:text-white font-normal">API Pricing</a>;
  const empty = "";
  const byokApiPricing = <>{byokOnly}<br />/<br />{apiPricingOnly}</>;
  const checkmark = <>
      <img className="block dark:hidden" src={"https://exafunction.github.io/public/icons/docs/checkmark-black.png"} alt="Available" style={{
    width: '16px',
    height: '16px',
    margin: '0 auto',
    pointerEvents: 'none'
  }} />
      <img className="hidden dark:block" src={"https://exafunction.github.io/public/icons/docs/checkmark-white.png"} alt="Available" style={{
    width: '16px',
    height: '16px',
    margin: '0 auto',
    pointerEvents: 'none'
  }} />
    </>;
  const models = [{
    name: "SWE-1.5",
    icon: windsurfIcon,
    credits: "1",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "SWE-1",
    icon: windsurfIcon,
    credits: "0",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Sonnet 4.5",
    icon: claudeIcon,
    credits: "2",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: "3x",
    trial: checkmark
  }, {
    name: "Claude Sonnet 4.5 (Thinking)",
    icon: claudeIcon,
    credits: "3",
    hasGift: true,
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: "4x",
    trial: checkmark
  }, {
    name: "Claude Haiku 4.5",
    icon: claudeIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Opus 4.1",
    icon: claudeIcon,
    credits: "20",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude Opus 4.1 Thinking",
    icon: claudeIcon,
    credits: "20",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (low reasoning)",
    icon: openaiIcon,
    credits: "0.5",
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (medium reasoning)",
    icon: openaiIcon,
    credits: "1",
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5 (high reasoning)",
    icon: openaiIcon,
    credits: "2",
    free: "1.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-5-Codex",
    icon: openaiIcon,
    credits: "0",
    hasGift: true,
    free: "0.5",
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Gemini 2.5 Pro",
    icon: geminiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "xAI Grok Code Fast",
    icon: grokIcon,
    credits: "0",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Kimi K2",
    icon: kimiIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "Qwen3-Coder Fast",
    icon: qwenIcon,
    credits: "2",
    hasGift: true,
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "Qwen3-Coder",
    icon: qwenIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "o3",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "o3 (high reasoning)",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude 3.7 Sonnet",
    icon: claudeIcon,
    credits: "2",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "1x",
    trial: byokOnly
  }, {
    name: "Claude 3.7 Sonnet (Thinking)",
    icon: claudeIcon,
    credits: "3",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "1.25x",
    trial: byokOnly
  }, {
    name: "Claude Sonnet 4",
    icon: claudeIcon,
    credits: "2",
    hasGift: true,
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "3x",
    trial: checkmark
  }, {
    name: "Claude Sonnet 4 (Thinking)",
    icon: claudeIcon,
    credits: "3",
    hasGift: true,
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: "4x",
    trial: checkmark
  }, {
    name: "gpt-oss 120B (Medium)",
    icon: openaiIcon,
    credits: "0.25",
    free: empty,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-4o",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "GPT-4.1",
    icon: openaiIcon,
    credits: "1",
    free: checkmark,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: checkmark
  }, {
    name: "Claude 3.5 Sonnet",
    icon: claudeIcon,
    credits: "2",
    free: byokOnly,
    pro: checkmark,
    teams: checkmark,
    enterprise: checkmark,
    trial: byokOnly
  }, {
    name: "Claude 4 Opus",
    icon: claudeIcon,
    credits: byokOnly,
    free: byokOnly,
    pro: byokOnly,
    teams: empty,
    enterprise: empty,
    trial: byokOnly
  }, {
    name: "Claude 4 Opus (Thinking)",
    icon: claudeIcon,
    credits: byokOnly,
    free: byokOnly,
    pro: byokOnly,
    teams: empty,
    enterprise: empty,
    trial: byokOnly
  }, {
    name: "DeepSeek-V3-0324",
    icon: deepseekIcon,
    credits: "0",
    free: empty,
    pro: checkmark,
    teams: empty,
    enterprise: empty,
    trial: checkmark
  }, {
    name: "DeepSeek-R1",
    icon: deepseekIcon,
    credits: "0.5",
    free: empty,
    pro: checkmark,
    teams: empty,
    enterprise: empty,
    trial: checkmark
  }];
  return <>
      <style>{`
        .gift-tooltip-container:hover .gift-tooltip {
          opacity: 1 !important;
          visibility: visible !important;
        }
        #table-container {
          overflow: visible !important;
          max-height: none !important;
          height: auto !important;
        }
        #models-table {
          overflow: visible !important;
          max-height: none !important;
          height: auto !important;
        }
        @media (max-width: 768px) {
          #table-container {
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
          }
          #models-table {
            min-width: 700px !important;
          }
        }
        #table-container * {
          overflow: visible !important;
        }
      `}</style>
      <div id="table-container" style={{
    width: 'auto',
    borderRadius: '8px',
    overflow: 'visible',
    maxHeight: 'none',
    height: 'auto'
  }} className="light:bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10">
        <table id="models-table" style={{
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '14px',
    tableLayout: 'auto',
    margin: '0',
    padding: '0',
    height: 'auto',
    maxHeight: 'none'
  }}>
          <thead style={{
    margin: '0',
    padding: '0'
  }}>
            <tr className="border-b border-black/10 dark:!border-white/10">
              <th style={{
    padding: '16px 16px',
    textAlign: 'left',
    fontWeight: '500',
    minWidth: '200px'
  }} className="text-gray-700 dark:text-white">Model</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '80px'
  }} className="text-gray-700 dark:text-white">Credits</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Free</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Pro</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '80px'
  }} className="text-gray-700 dark:text-white">Teams</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '120px'
  }} className="text-gray-700 dark:text-white">Enterprise</th>
              <th style={{
    padding: '16px 8px',
    textAlign: 'center',
    fontWeight: '500',
    minWidth: '60px'
  }} className="text-gray-700 dark:text-white">Trial</th>
            </tr>
          </thead>
          <tbody style={{
    margin: '0',
    padding: '0'
  }}>
            {models.filter((model, index) => showAll || index < 12).map((model, index, filteredArray) => <tr key={model.name} className={`${index === filteredArray.length - 1 ? '' : 'border-b border-black/10 dark:!border-white/10'}`}>
                <td style={{
    padding: '8px',
    fontWeight: '500',
    verticalAlign: 'middle'
  }}>
                  <div style={{
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    whiteSpace: 'nowrap'
  }}>
                    <span style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '20px',
    height: '20px',
    flexShrink: 0
  }}>
                      <img className="block dark:hidden" src={model.icon.light} alt={`${model.name} icon`} style={{
    width: '20px',
    height: '20px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                      <img className="hidden dark:block" src={model.icon.dark} alt={`${model.name} icon`} style={{
    width: '20px',
    height: '20px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                    </span>
                    <span className="text-gray-700 dark:text-white">{model.name}</span>
                  </div>
                </td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>
                  <div style={{
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px'
  }}>
                    <span className="text-gray-700 dark:text-white">{model.credits}</span>
                    {model.hasGift && <div className="gift-tooltip-container" style={{
    position: 'relative',
    display: 'inline-flex'
  }}>
                        <span style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '16px',
    height: '16px'
  }}>
                          <img className="block dark:hidden" src="https://exafunction.github.io/public/icons/docs/gift-black.png" alt="Gift icon" style={{
    width: '16px',
    height: '16px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                          <img className="hidden dark:block" src="https://exafunction.github.io/public/icons/docs/gift-white.png" alt="Gift icon" style={{
    width: '16px',
    height: '16px',
    objectFit: 'contain',
    pointerEvents: 'none',
    userSelect: 'none'
  }} />
                        </span>
                        <div className="gift-tooltip" style={{
    position: 'absolute',
    bottom: '100%',
    left: '50%',
    transform: 'translateX(-50%)',
    marginBottom: '8px',
    padding: '8px 12px',
    backgroundColor: '#333',
    color: 'white',
    borderRadius: '6px',
    fontSize: '12px',
    whiteSpace: 'nowrap',
    opacity: '0',
    visibility: 'hidden',
    transition: 'opacity 0.2s, visibility 0.2s',
    zIndex: '1000',
    pointerEvents: 'none'
  }}>
                          Promo pricing only available for a limited time
                          <div style={{
    position: 'absolute',
    top: '100%',
    left: '50%',
    transform: 'translateX(-50%)',
    width: '0',
    height: '0',
    borderLeft: '5px solid transparent',
    borderRight: '5px solid transparent',
    borderTop: '5px solid #333'
  }}></div>
                        </div>
                      </div>}
                  </div>
                </td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.free}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.pro}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.teams}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.enterprise}</td>
                <td style={{
    padding: '10px',
    textAlign: 'center',
    verticalAlign: 'middle'
  }}>{model.trial}</td>
              </tr>)}
          </tbody>
        </table>
      </div>
      <div style={{
    display: 'flex',
    justifyContent: 'center',
    padding: '16px 0',
    borderTop: 'none'
  }}>
        <button onClick={() => {
    if (!showAll) {
      setShowAll(true);
    } else {
      setShowAll(false);
    }
  }} style={{
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '10px 20px',
    backgroundColor: 'transparent',
    border: '1px solid #868686',
    borderRadius: '8px',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    minWidth: '140px'
  }} className="text-gray-700 hover:bg-gray-50 dark:border-gray-600 dark:text-white dark:hover:bg-gray-800">
          {showAll ? 'Show Less Models' : 'Show More Models'}
        </button>
      </div>
    </>;
};

In Cascade, you can easily switch between different models of your choosing.

Depending on the model you select, each of your input prompts will consume a different number of [prompt credits](/windsurf/cascade/usage).

Under the text input box, you will see a model selection dropdown menu containing the following models:

<ModelsTable />

---

← Previous: [Windsurf Guide for Enterprise Admins](./windsurf-guide-for-enterprise-admins.md) | [Index](./index.md) | Next: [SWE-1.5, swe-grep, SWE-1](./swe-15-swe-grep-swe-1.md) →