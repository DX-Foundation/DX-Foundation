using System;
using Exiled.API.Features;

namespace GhostSCP
{
    public class Plugin : Exiled.API.Features.Plugin<Config>
    {
        public override string Name => "GhostSCP";
        public override string Author => "DX Foundation";
        public override Version Version => new Version("3.0.0");
        
        // 🎃 DX FOUNDATION PLUGIN
        public override void OnEnabled()
        {
            Log.Info("🎃 DX Foundation Plugin активирован!");
            Log.Info("👻 GhostSCP готов к работе!");
            Log.Info("🏢 Организация: DX Foundation");
            base.OnEnabled();
        }
        
        public override void OnDisabled()
        {
            Log.Info("💀 GhostSCP отключен!");
            base.OnDisabled();
        }
    }
    
    public class Config : Exiled.API.Interfaces.IConfig
    {
        public bool IsEnabled { get; set; } = true;
        public bool Debug { get; set; } = false;
        public string Organization { get; set; } = "DX Foundation";
    }
}
